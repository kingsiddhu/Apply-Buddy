import requests
import Scripts.debug

def get_working_server(servers, timeout=5):
    """
    Try each server in order and return the first one that responds
    without a connection/timeout error.

    A server counts as "working" if we can reach it at all -- we don't
    care about the exact status code (a 404 on the bare base URL is
    fine, it still means the host is up). Only network-level failures
    (can't connect, DNS failure, timeout) disqualify a server.

    :param servers: list of base URLs, e.g.
        ["http://localhost:2000", "https://latex.ytotech.com"]
    :param timeout: seconds to wait per server before giving up
    :return: the first reachable base URL (str), or None if none work
    """
    for base_url in servers:
        try:
            x = requests.get(base_url, timeout=timeout)
            # Any response at all (even 4xx/5xx) means the server is up.
            x = str(x.content)
            print(x)
            if x[2]=="{":
                if "texlive_version" in Scripts.parsejson.extract_json(x):
                    return base_url
            else:
                continue
        except requests.exceptions.RequestException as e:
            print(f"[skip] {base_url} unreachable: {e}")
            continue

    return None

def compile_latex_to_pdf(server_url, data, output_path, endpoint="/builds/sync", timeout=120):
    """
    POST a LaTeX build request to a working server and save the returned
    PDF to disk.

    :param server_url: base URL returned by get_working_server()
    :param data: dict matching the LaTeX-on-HTTP JSON schema, e.g.
        {
            "compiler": "pdflatex",
            "resources": [{"main": True, "content": "..."}]
        }
    :param output_path: where to save the resulting PDF, e.g. "out.pdf"
    :param endpoint: API path for the sync build endpoint
    :param timeout: seconds to wait for compilation
    :return: output_path on success, None on failure
    """
    url = server_url.rstrip("/") + endpoint

    try:
        headers = {"Content-Type": "application/json"}
        if "ngrok" in server_url:
            headers['ngrok-skip-browser-warning'] = 'true'
            headers["User-Agent"] = "CustomAPIClient/1.0"
        Scripts.debug.logger(headers)
        response = requests.post(
            url,
            json=data,
            headers=headers,
            timeout=timeout,
        )
    except requests.exceptions.RequestException as e:
        print(f"[error] request to {url} failed: {e}")
        return None

    content_type = response.headers.get("Content-Type", "")

    if response.status_code == 201 and "application/pdf" in content_type:
        #Got the needed pdf result
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"[ok] PDF saved to {output_path}")
        return output_path

    # Compilation errors from LaTeX-on-HTTP comes back not as a PDF. (prob json)
    print(f"[error] build failed (status {response.status_code}): {str(response.text).replace("\\n", "\n")}")
    return None

