import flask_wtf
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html

class Form(flask_wtf.Form):
    match_id = IntegerField('Match #', buttons=False)
    team_id = IntegerField('Team #', buttons=False)
    #Form Fields
        auton_start = RadioField('Robot Starting Location',choices=[('Neutral Zone','Neutral Zone'), ('Courtyard','Courtyard')],
                             default='Neutral Zone')
    auton_breach = RadioField('Defense Crossed in Auton', choices=[('0','None'),
                                                                   ('1','Touched'),
                                                                   ('2','Crossed (Mark the defense in the Teleop section)')],
                                                                   default='0')
    auton_score = RadioField('Ball Scored', choices=[('0','None'), ('1','Low Goal'), ('2','High Goal')],
                             default='0')
    comments = TextAreaField('', col_md=12)

