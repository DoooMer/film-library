from peewee_validates import ModelValidator, StringField, IntegerField, validate_not_empty


class FilmValidator(ModelValidator):
    title = StringField(validators=[validate_not_empty()], required=True)
    year = IntegerField(required=True)

    class Meta:
        messages = {
            'title.empty': "\"Название\" не заполнено",
            'year.coerce_int': "\"Год выхода\" не заполнено"
        }
