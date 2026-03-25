from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import json
from utils import generate_uuid, generate_timestamp

# Setup the Jinja environment to load templates
env = Environment(
    loader=FileSystemLoader(
        Path(__file__).resolve().parent.parent / "assets" / "templates"
    )
)

env.globals['uuid'] = generate_uuid
env.globals['timestamp'] = generate_timestamp

# Load the specific template file
template = env.get_template('components/base.xml.j2')

# Define the data you want to inject
base_path = Path(__file__).resolve().parent.parent
json_path = base_path / "assets" / "mappings" / "mon-mothma-covid.json"
with open(json_path) as f:
    data = json.load(f)

xml_nsmap = {
        None: "urn:hl7-org:v3",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "sdtc": "urn:hl7-org:sdtc",
        "voc": "http://www.lantanagroup.com/voc",
        "schema_location": "urn:hl7-org:v3 ../../schema/infrastructure/cda/CDA_SDTC.xsd"
    }

# Render the template with your data
rendered_xml = template.render(data, nsmap=xml_nsmap)

# 5. Save the output to a new XML file
with open("output.xml", "w", encoding="utf-8") as f:
    f.write(rendered_xml)

print("XML file generated successfully!")
