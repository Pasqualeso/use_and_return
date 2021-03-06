from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DateField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

# classe form registrazione annuncio
from wtforms.widgets import TextArea


class RegistrationFormAnnuncio(FlaskForm):
    titolo_annuncio = StringField("Inserisci il titolo dell'annuncio", validators=[DataRequired(), Length(1, 64)])
    categoria_annuncio = SelectField(
        "Inserisci la categoria dell'annuncio",
        choices=[("musica", "Musica"), ("telefonia", "Telefonia"), ("console_e_videogiochi", "Console e videogiochi"),
                 ("informatica", "Informatica"),
                 ("auto", "Accessori auto"), ("giocattoli", "Giocattoli"), ("fotografia", "Fotografia"),
                 ("videomaker", "Video-maker"), ("altro", "Altro")]
        , validators=[DataRequired()])

    immagine_annuncio = FileField("Inserisci un'immagine", validators=[DataRequired()])

    prezzo_per_giorno_annuncio = IntegerField("Inserisci il prezzo al giorno per l'annuncio",
                                              validators=[DataRequired()])
    descrizione_annuncio = TextAreaField("Inserisci una descrizione (Max 200 caratteri)",
                                         validators=[DataRequired(), Length(1, 200)])

    data_inizio_noleggio_annuncio = DateField("Inserisci una data di inizio noleggio", format='%Y-%m-%d',
                                              validators=[DataRequired()])
    data_fine_noleggio_annuncio = DateField("Inserisci una data di fine noleggio", format='%Y-%m-%d',
                                            validators=[DataRequired()])

    citta_annuncio = StringField("Inserisci la città dell'annuncio",
                                 validators=[DataRequired(message='Città obbligatoria'), Length(1, 64)])

    provincia_annuncio = SelectField(
        "Inserisci la provincia dell'annuncio",
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

    via_annuncio = StringField("Inserisci la via dell'annuncio", validators=[DataRequired()])
    cap_annuncio = IntegerField("Inserisci il cap dell'annuncio", validators=[DataRequired()])

    submit_annuncio = SubmitField("Aggiungi")
