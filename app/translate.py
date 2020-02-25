import requests
from flask_babel import _
from flask import current_app

ms_translator_url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}"


def translate(text, source_language, dest_language):
    if "MS_TRANSLATOR_KEY" not in current_app.config or not current_app.config["MS_TRANSLATOR_KEY"]:
        return _("Error: the translation service is not configured")
    auth = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    url = ms_translator_url.format(source_language, dest_language)
    resp = requests.post(url=url, json=[{"Text": text}], headers=auth)
    if resp.status_code != 200:
        return _('Error: the translation service failed.')
    json_data = resp.json()  # json.loads(resp.content.decode("utf-8-sig"))
    translated_text = json_data[0]["translations"][0]["text"]
    return translated_text


