from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, EmailField, DateField, IntegerField, \
    FileField, BooleanField
from wtforms.validators import EqualTo, DataRequired, Email, ValidationError, Length

# classe form login utente
from project.utenti.models import Utente


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField('Ricordami su questo sito')
    submit_login = SubmitField("Submit")


################################################
# classe form registrazione utente
class RegistrationForm(FlaskForm):
    id_utente = StringField("Id")
    nome_utente = StringField("Inserisci il tuo nome", validators=[DataRequired()])
    cognome_utente = StringField("Inserisci il tuo cognome", validators=[DataRequired()])
    email = EmailField("Inserisci la tua email", validators=[DataRequired()])
    username = StringField("Inserisci il tuo username", validators=[DataRequired()])
    password = PasswordField("Inserisci la tua password", validators=[DataRequired()])
    sesso = SelectField(
        "Inserisci il tuo sesso: ",
        choices=[("m", "M"), ("f", "F"), ("n", "N")]
        , validators=[DataRequired()]
    )
    telefono = StringField("Inserisci il tuo numero di telefono", validators=[DataRequired()])
    data_di_nascita = DateField("Inserisci la data di nascita", format='%Y-%m-%d', validators=[DataRequired()])
    citta = StringField("Inserisci la citta", validators=[DataRequired()])
    provincia = SelectField(
        "Inserisci la provincia",
        choices=[("ag", "Agrigento"), ("al", "Alessandria"), ("an", "Ancona"), ("ao", "Aosta"), ("ar", "Arezzo"),
                 ("ap", "Ascoli Piceno"),
                 ("at", "Asti"), ("av", "Avellino"), ("ba", "Bari"), ("bt", "Barletta-Andria-Trani"), ("bl", "Belluno"),
                 ("bn", "Benevento"),
                 ("bg", "Bergamo"), ("bi", "Biella"), ("bo", "Bologna"), ("bz", "Bolzano"), ("bs", "Brescia"),
                 ("br", "Brindisi"), ("ca", "Cagliari"),
                 ("cl", "Caltanissetta"), ("cb", "Campobasso"), ("ci", "Carbonia - iglesias "), ("ce", "Caserta"),
                 ("ct", "Catania"), ("cz", "Catanzaro"),
                 ("ch", "Chieti"), ("co", "Como"), ("cs", "Cosenza"), ("cr", "Cremona"), ("kr", "Crotone"),
                 ("cn", "Cuneo"), ("en", "Enna"), ("fm", "Fermo"),
                 ("fe", "Ferrara"), ("fi", "Firenze"), ("fg", "Foggia"), ("fc", "Forli-Cesena"), ("fr", "Frosinone"),
                 ("ge", "Genova"), ("go", "Gorizia"),
                 ("gr", "Grosseto"), ("im", "Imperia"), ("is", "Isernia"), ("sp", "La spezia"), ("aq", "L'aquila"),
                 ("lt", "Latina"), ("le", "Lecce"),
                 ("lc", "Lecco"), ("li", "Livorno"), ("lo", "Lodi"), ("lu", "Lucca"), ("mc", "Macerata"),
                 ("mn", "Mantova"), ("ms", "Massa - Carrara"),
                 ("mt", "Matera"), ("vs", "Medio Campidano"), ("me", "Messina"), ("mi", "Milano"), ("mo", "Modena"),
                 ("mb", "Monza e della Brianza"),
                 ("na", "Napoli"), ("no", "Novara"), ("nu", "Nuoro"), ("og", "Ogliastra"), ("ot", "Olbia - Tempio"),
                 ("or", "Oristano"), ("pd", "Padova"),
                 ("pa", "Palermo"), ("pr", "Parma"), ("pv", "Pavia"), ("pg", "Perugia"), ("pu", "Pesaro e Urbino"),
                 ("pe", "Pescara"), ("pc", "Piacenza"),
                 ("pi", "Pisa"), ("pt", "Pistoia"), ("pn", "Pordenone"), ("pz", "Potenza"), ("po", "Prato"),
                 ("rg", "Ragusa"), ("ra", "Ravenna"), ("rc", "Reggio di Calabria"),
                 ("re", "Reggio nell'Emilia"), ("ri", "Rieti"), ("rn", "Rimini"), ("rm", "Roma"), ("ro", "Rovigo"),
                 ("sa", "Salerno"), ("ss", "Sassari"),
                 ("sv", "Savona"), ("si", "Siena"), ("sr", "Siracusa"), ("so", "Sondrio"), ("ta", "Taranto"),
                 ("te", "Teramo"), ("tr", "Terni"), ("to", "Torino"),
                 ("tp", "Trapani"), ("tn", "Trento"), ("tv", "Treviso"), ("ts", "Trieste"), ("ud", "Udine"),
                 ("va", "Varese"), ("ve", "Venezia"), ("vb", "Verbano - Cusio - Ossola "),
                 ("vc", "Vercelli"), ("vr", "Verona"), ("vv", "ibo valentia"), ("vi", "Vicenza"), ("vt", "Viterbo")]
        , validators=[DataRequired()])
    via = StringField("Inserisci la via", validators=[DataRequired()])
    cap = StringField("Inserisci il cap", validators=[DataRequired()])

    submit = SubmitField("Submit")


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Vecchia password', validators=[DataRequired(message='Vecchia password obbligatoria')])
    password = PasswordField('Nuova password', validators=[
        DataRequired(message='Nuova password obbligatoria'), EqualTo('password2', message='Le due passwords devono essere uguali')])
    password2 = PasswordField('Conferma nuova password',
                              validators=[DataRequired(message='Conferma nuova password obbligatoria')])
    submit = SubmitField('Aggiorna password')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email obbligatoria'), Length(1, 64),
                                             Email(message="Email non valida")])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Nuova password', validators=[
        DataRequired(message='Nuova password obbligatoria'), EqualTo('password2', message='Le due passwords devono essere uguali')])
    password2 = PasswordField('Conferma password', validators=[DataRequired(message='Conferma nuova password obbligatoria')])
    submit = SubmitField('Reset Password')


class ChangeEmailForm(FlaskForm):
    email = StringField('Nuova Email', validators=[DataRequired(message='Nuova email obbligatoria'), Length(1, 64),
                                                 Email(message="Email non valida")])
    password = PasswordField('Password', validators=[DataRequired(message='Password obbligatoria')])
    submit = SubmitField('Email aggiornata')

    def validate_email(self, field):
        if Utente.query.filter_by(email=field.data.lower()).first():
            raise ValidationError(u'Email già registrata.')

# classe form registrazione annuncio
class RegistrationFormAnnuncio(FlaskForm):
    titolo_annuncio = StringField("Inserisci il titolo della categoria", validators=[DataRequired()])
    categoria_annuncio = SelectField(
        "Inserisci la categoria",
        choices=[("musica", "Musica"), ("telefonia", "Telefonia"), ("console e videogiochi", "Console e videogiochi"),
                 ("informatica", "Informatica"),
                 ("accessori auto", "Accessori auto"), ("giocattoli", "Giocattoli"), ("fotografia", "Fotografia"),
                 ("video-maker", "Video-maker"), ("altro", "Altro")]
        , validators=[DataRequired()])
    descrizione_annuncio = StringField("Inserisci una descrizione(Max 200 caratteri)", validators=[DataRequired()])
    regione_annuncio =SelectField(
        "Inserisci la regione dell'annuncio",
        choices=[("valle d'aosta", "Valle d'Aosta"), ("piemonte", "Piemonte"), ("liguria", "Liguria"),
                 ("lombardia", "Lombardia"), ("trentino-alto adige", "Trentino-Alto Adige"),
                 ("veneto", "Veneto"), ("friuli-venezia giulia", "Friuli-Venezia Giulia"),
                 ("emilia romagna", "Emilia Romagna"), ("toscana", "Toscana"), ("umbria", "Umbria"),
                 ("marche", "Marche"),
                 ("lazio", "Lazio"), ("abruzzo", "Abruzzo"), ("molise", "Molise"), ("campania", "Campania"),
                 ("puglia", "Puglia"), ("basilicata", "Basilicata"), ("calabria", "Calabria"),
                 ("sicilia", "Sicilia"), ("sardegna", "Sardegna"), ("non specificare", "Non Specificare"), ]

        , validators=[DataRequired()])

    prezzo_per_giorno_annuncio = IntegerField("Inserisci il prezzo al giorno per l'annuncio", validators=[DataRequired()])

    data_inizio_noleggio_annuncio = DateField("Inserisci una data di inizio noleggio", validators=[DataRequired()])
    data_fine_noleggio_annuncio = DateField("Inserisci una data di fine noleggio", validators=[DataRequired()])
    disponibile = IntegerField("Inserisci la disponibilità", validators=[DataRequired()])

    immagine_annuncio = FileField("Inserisci un'immagine", validators=[DataRequired()])

    submit_annuncio = SubmitField("Submit")


# classe form barra di ricerca in index
class RegistrationFormRicerca(FlaskForm):
    oggetto_ricerca = StringField("Inserisci oggetto)", validators=[DataRequired()])
    categoria_ricerca = SelectField(
        "Inserisci la categoria",
        choices=[("musica", "Musica"), ("telefonia", "Telefonia"), ("console e videogiochi", "Console e videogiochi"),
                 ("informatica", "Informatica"),
                 ("accessori auto", "Accessori auto"), ("giocattoli", "Giocattoli"), ("fotografia", "Fotografia"),
                 ("video-maker", "Video-maker"), ("altro", "Altro")]
        , validators=[DataRequired()])
    regione_ricerca = SelectField(
        "Inserisci la regione",
        choices=[("valle d'aosta", "Valle d'Aosta"), ("piemonte", "Piemonte"), ("liguria", "Liguria"),
                 ("lombardia", "Lombardia"), ("trentino-alto adige", "Trentino-Alto Adige"),
                 ("veneto", "Veneto"), ("friuli-venezia giulia", "Friuli-Venezia Giulia"),
                 ("emilia romagna", "Emilia Romagna"), ("toscana", "Toscana"), ("umbria", "Umbria"),
                 ("marche", "Marche"),
                 ("lazio", "Lazio"), ("abruzzo", "Abruzzo"), ("molise", "Molise"), ("campania", "Campania"),
                 ("puglia", "Puglia"), ("basilicata", "Basilicata"), ("calabria", "Calabria"),
                 ("sicilia", "Sicilia"), ("sardegna", "Sardegna"), ("non specificare", "Non Specificare"), ]

        , validators=[DataRequired()])
    data_inizio_noleggio_ricerca = DateField("Inserisci una data di inizio noleggio", validators=[DataRequired()])
    data_fine_noleggio_ricerca = DateField("Inserisci una data di fine noleggio", validators=[DataRequired()])

    submit_ricerca = SubmitField("Submit")
