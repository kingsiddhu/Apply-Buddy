import json

INIT_PROMPT="""
You are an AI agent designed to read through a description and fill the given placeholder \
data and only respond with json data and nothing else.
- Stick to the given placeholder names only. Do not modify names.
- Do NOT make up data if you were not given prior information
- Do not write paragraphs unless specified.
- Keep values short as these are only values to be placed in place of placeholders within sentences unless specified. 
- lowercased placeholders choices are keys that are used to refer to other dictionaries and thus must be unchanged.
The following choices are available to use as values of the lowercased placeholders: """

FORMAT="""\n 
These choices are direct values for the lowercased placeholders and cannot be expanded nor modified. 
These choices are also the topics the student is familiar with for reference.
Experience and field can be multiple topics the student is familiar with and can be flexible.
Format of output:
{
    "placeholder 1": "value 1",
    "PLACEHOLDER 2": "value 2",
}
"""
