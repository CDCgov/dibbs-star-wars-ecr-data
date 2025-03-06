from lxml import etree
from conftest import normalize_xml


def test_patient_template(jinja_env, patient_data, xml_nsmap, base_path):
    """Test that our template generates the expected patient XML structure."""
    # load and render the template
    template = jinja_env.get_template("components/patient.xml.j2")
    rendered_xml = template.render(
        patient=patient_data["components"]["patient"], nsmap=xml_nsmap
    )

    # load and extract the expected xml
    xml_path = base_path / "tests" / "assets" / "mon-mothma-covid-problem_eicr.xml"
    tree = etree.parse(str(xml_path))
    record_target = tree.find(".//{urn:hl7-org:v3}recordTarget")
    expected_xml = etree.tostring(record_target, encoding="unicode")

    # compare normalized versions
    normalized_rendered = normalize_xml(rendered_xml)
    normalized_expected = normalize_xml(expected_xml)

    # for debugging, print both versions if they don't match
    try:
        assert normalized_rendered == normalized_expected
    except AssertionError:
        print("\nNormalized Generated XML:")
        print(normalized_rendered)
        print("\nNormalized Expected XML:")
        print(normalized_expected)
        raise


def test_author_template(jinja_env, patient_data, xml_nsmap, base_path):
    """Test that our template generates the expected author XML structure."""
    # load and render the template
    template = jinja_env.get_template("components/author.xml.j2")
    rendered_xml = template.render(
        author=patient_data["components"]["author"], nsmap=xml_nsmap
    )

    # load and extract the expected xml
    xml_path = base_path / "tests" / "assets" / "mon-mothma-covid-problem_eicr.xml"
    tree = etree.parse(str(xml_path))
    author = tree.find(".//{urn:hl7-org:v3}author")
    expected_xml = etree.tostring(author, encoding="unicode")

    # compare normalized versions
    normalized_rendered = normalize_xml(rendered_xml)
    normalized_expected = normalize_xml(expected_xml)

    # for debugging, print both versions if they don't match
    try:
        assert normalized_rendered == normalized_expected
    except AssertionError:
        print("\nNormalized Generated XML:")
        print(normalized_rendered)
        print("\nNormalized Expected XML:")
        print(normalized_expected)
        raise


def test_custodian_template(jinja_env, patient_data, xml_nsmap, base_path):
    """Test that our template generates the expected custodian XML structure."""
    # load and render the template
    template = jinja_env.get_template("components/custodian.xml.j2")
    rendered_xml = template.render(
        facility=patient_data["components"]["facility"], nsmap=xml_nsmap
    )

    # load and extract the expected xml
    xml_path = base_path / "tests" / "assets" / "mon-mothma-covid-problem_eicr.xml"
    tree = etree.parse(str(xml_path))
    custodian = tree.find(".//{urn:hl7-org:v3}custodian")
    expected_xml = etree.tostring(custodian, encoding="unicode")

    # compare normalized versions
    normalized_rendered = normalize_xml(rendered_xml)
    normalized_expected = normalize_xml(expected_xml)

    # for debugging, print both versions if they don't match
    try:
        assert normalized_rendered == normalized_expected
    except AssertionError:
        print("\nNormalized Generated XML:")
        print(normalized_rendered)
        print("\nNormalized Expected XML:")
        print(normalized_expected)
        raise


def test_participant_template(jinja_env, patient_data, xml_nsmap, base_path):
    """Test that our template generates the expected participant XML structure.
    Participant is used in the eCR XML for emergency contact data."""
    # load and render the template
    template = jinja_env.get_template("components/participant.xml.j2")
    rendered_xml = template.render(
        participant=patient_data["components"]["participant"], nsmap=xml_nsmap
    )

    # load and extract the expected xml
    xml_path = base_path / "tests" / "assets" / "mon-mothma-covid-problem_eicr.xml"
    tree = etree.parse(str(xml_path))
    participant = tree.find(".//{urn:hl7-org:v3}participant")
    expected_xml = etree.tostring(participant, encoding="unicode")

    # compare normalized versions
    normalized_rendered = normalize_xml(rendered_xml)
    normalized_expected = normalize_xml(expected_xml)

    # for debugging, print both versions if they don't match
    try:
        assert normalized_rendered == normalized_expected
    except AssertionError:
        print("\nNormalized Generated XML:")
        print(normalized_rendered)
        print("\nNormalized Expected XML:")
        print(normalized_expected)
        raise