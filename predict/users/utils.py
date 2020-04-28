import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from predict import app, mail

def save_picture(form_picture):
    rnd_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = rnd_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request', 
                    sender='noreply@demo.com', 
                    recipients=[user.email])
    msg.body = f'''To reset you password visit the following link:
    {url_for('users.reset_token', token=token, _external=True)}

    If you did not make this request then simply ignore this email.
    '''
    mail.send(msg)