highrise
=============

python-highrise is a way to wrap Highrise's API Pythonically.

Installation
-----------

    easy_install ElementTree https://github.com/chriscohoat/highrise/tarball/master


Usage
-----

    # Import the highrise wrapper.
    from highrise.wrapper import Highrise
    
    #Prepare the Highrise interaction with the API token and person ID
    highrise_api_token = 'TOKEN_HERE'
    person_highrise_id = 'PERSON_ID_HERE'
    hr = Highrise('https://examplecorporation.highrisehq.com',highrise_api_token)
    
    #Get list of notes or list of emails
    notes = hr.notes(person_highrise_id)
    emails = hr.emails(person_highrise_id)
    
Interacting with notes (in a Django template)
-----

    {% if not notes %}
    <h3>No notes available for this candidate.</h3>
    {% else %}
    {% for note in notes %}
    
    <h3>Note about {{ note.subject_name }}</h3>
    <h4>Added at {{ note.created_at }}</h4>
	<p>
		{{ note.body }}
		<br />
		<br />
		<a href="https://examplecorporation.highrisehq.com/notes/{{ note.note_id }}" target="blank">Read More...</a>
	</p>
	
	{% endfor %}
	{% endif %}

Testing
-------

More to come with testing.

