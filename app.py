import streamlit as st
import pandas as pd
import joblib
import datetime

# Load model and column info
model, num_cols, cat_cols = joblib.load("gb_model_bundle.pkl")

st.set_page_config(page_title="F1 Finish Predictor", page_icon="🏎️", layout="centered")
st.title(" F1 Race Finish Position Predictor")

st.markdown("""
This app predicts the **finish position** of a Formula 1 driver based on race details, car constructor, and other key parameters.
""")

# Example dropdown options (replace with your real data lists if available)
driver_options = ['raikkonen', 'watson', 'ruttman', 'mick_schumacher', 'modena',
       'kevin_magnussen', 'mario_andretti', 'gutierrez', 'hamilton',
       'ireland', 'brundle', 'wendlinger', 'johansson', 'gachot',
       'kobayashi', 'cesaris', 'jarier', 'max_verstappen', 'ickx',
       'alguersuari', 'borgudd', 'cecotto', 'moreno', 'tambay', 'alesi',
       'rebaque', 'arnoux', 'dalmas', 'fangio', 'redman', 'senna',
       'perez', 'bernard', 'capelli', 'laffite', 'grosjean', 'moser',
       'mclaren', 'keke_rosberg', 'sutton', 'lauda', 'michael_schumacher',
       'bonnier', 'alliot', 'caffi', 'alonso', 'satoru_nakajima', 'rindt',
       'patrese', 'vettel', 'trulli', 'ahrens', 'herbert', 'pirro',
       'ocon', 'mansell', 'schneider', 'lees', 'cevert', 'blundell',
       'fitch', 'beretta', 'petrov', 'surer', 'coulthard', 'verstappen',
       'bertaggia', 'moss', 'rosberg', 'damon_hill', 'gregory', 'buemi',
       'villeneuve', 'daly', 'sutil', 'martini', 'katayama', 'kinnunen',
       'emerson_fittipaldi', 'lammers', 'irvine', 'mazepin', 'morbidelli',
       'panis', 'peterson', 'webber', 'palm', 'manfred_winkelhock',
       'hoffmann', 'guerrero', 'de_vries', 'adamich', 'fagioli', 'wilds',
       'ericsson', 'glock', 'frentzen', 'siffert', 'piastri', 'berger',
       'hulme', 'sala', 'revson', 'mantovani', 'tsunoda', 'ashley',
       'nasr', 'prost', 'ricciardo', 'salazar', 'sainz', 'reutemann',
       'button', 'zonta', 'sullivan', 'brudes', 'ralf_schumacher',
       'heidfeld', 'davidson', 'stewart', 'brise', 'nannini', 'schell',
       'pryce', 'jack_brabham', 'hawthorn', 'stevenson', 'bandini',
       'boesel', 'warwick', 'settember', 'piquet', 'massa', 'streiff',
       'jules_bianchi', 'maldonado', 'stohr', 'cheever', 'surtees',
       'hakkinen', 'fittipaldi', 'trintignant', 'boutsen', 'alboreto',
       'gene', 'keegan', 'russell', 'kubica', 'beaufort', 'rathmann',
       'nakajima', 'barrichello', 'binder', 'sommer', 'grouillard',
       'palmer', 'sato', 'castellotti', 'norris', 'montoya', 'bottas',
       'diniz', 'gamble', 'andretti', 'chilton', 'baldi', 'stommelen',
       'grassi', 'maglioli', 'comas', 'wilson', 'piquet_jr', 'leclerc',
       'nilsson', 'kovalainen', 'lehto', 'angelis', 'fisichella', 'salo',
       'hulkenberg', 'mcnish', 'gugelmin', 'etancelin', 'ginther',
       'kessel', 'mass', 'giacomelli', 'clark', 'liuzzi', 'claes',
       'kvyat', 'pizzonia', 'stuck', 'stroll', 'colapinto', 'gendebien',
       'fabi', 'schenken', 'speed', 'collins', 'jabouille',
       'trevor_taylor', 'bira', 'salvadori', 'larini', 'boullion',
       'oliver', 'gurney', 'rosa', 'dick_rathmann', 'scarlatti', 'musso',
       'ghinzani', 'branson', 'hill', 'rosset', 'badoer', 'darter',
       'yamamoto', 'pescarolo', 'ribeiro', 'depailler', 'nakano',
       'scott_Brown', 'beltoise', 'giovinazzi', 'ganley', 'latifi',
       'pironi', 'phil_hill', 'menditeguy', 'campos', 'gilles_villeneuve',
       'love', 'jones', 'burgess', 'pretorius', 'rodriguez',
       'graffenried', 'lawson', 'montermini', 'regazzoni',
       'schiattarella', 'pace', 'takahashi', 'wharton', 'brendon_hartley',
       'gaillard', 'fairman', 'farina', 'gasly', 'thomson', 'helfrich',
       'resta', 'galvez', 'chandhok', 'amon', 'wurz', 'albon', 'perdisa',
       'henton', 'mieres', 'bernoldi', 'schlesser', 'serra', 'bailey',
       'galli', 'mcalpine', 'garde', 'burti', 'merzario', 'hattori',
       'roig', 'arundell', 'dempsey_wilson', 'behra', 'weyant', 'irwin',
       'zanardi', 'pesenti_rossi', 'gounon', 'alan_brown', 'albers',
       'dusio', 'parkes', 'courage', 'paul_russo', 'wacker', 'hunt',
       'ascari', 'wehrlein', 'gethin', 'bleekemolen', 'marko', 'rosier',
       'migault', 'larson', 'daponte', 'hansgen', 'bruno_senna', 'lunger',
       'joachim_winkelhock', 'taruffi', 'karthikeyan', 'gardner',
       'stevens', 'sargeant', 'foitek', 'weidler', 'gonzalez', 'lamy',
       'chiron', 'craft', 'heyer', 'naspetti', 'manzon', 'mcgrath',
       'tarquini', 'miles', 'hailwood', 'godia', 'maggs', 'inoue', 'bell',
       'vergne', 'pantano', 'larrauri', 'marimon', 'simon', 'klien',
       'piotti', 'magill', 'monteiro', 'oscar_gonzalez', 'paletti',
       'brambilla', 'doornbos', 'danner', 'hall', 'suzuki', 'shelby',
       'marques', 'mairesse', 'beuttler', 'eaton', 'scheckter', 'berg',
       'rolt', 'wilson_fittipaldi', 'chaves', 'schindler',
       'ian_scheckter', 'bryan', 'filippis', 'tuero', 'scarfiotti',
       'zhou', 'purley', 'papis', 'brooks', 'cabantous', 'elford',
       'stacey', 'matta', 'jimmy_stewart', 'bianco', 'acheson',
       'dumfries', 'attwood', 'daigh', 'barber', 'andersson', 'bearman',
       'ayulo', 'bettenhausen', 'cheesbourg', 'wietzes', 'bondurant',
       'vandoorne', 'nazaruk', 'picard', 'raphanel', 'kozarowitzky',
       'donohue', 'fischer', 'poele', 'takagi', 'shelly', 'brabham',
       'brandon', 'ambrosio', 'lucienbonnet', 'gaze', 'agabashian',
       'amick', 'flinterman', 'belmondo', 'murray', 'gerini', 'lavaggi',
       'corrado_fabi', 'portago', 'gould', 'spence', 'gabbiani', 'gavin',
       'serrurier', 'reg_parnell', 'wisell', 'barbazza', 'sirotkin',
       'teague', 'ertl', 'perkins', 'whitehead', 'reventlow', 'pic',
       'trips', 'haryanto', 'wallard', 'villoresi', 'mazzacane',
       'donnelly', 'baghetti', 'mackay-fraser', 'ward', 'lombardi',
       'bonetto', 'fonder', 'linden', 'freeland', 'hampshire', 'ligier',
       'ulmen', 'wunderink', 'lof', 'hartley', 'harrison', 'bellof',
       'londono', 'jolyon_palmer', 'larreta', 'fabre', 'kladis', 'merhi',
       'lewis', 'opel', 'johnson', 'langes', 'naylor', 'turner', 'byrne',
       'faulkner', 'boyd', 'bartels', 'campbell-jones', 'reece', 'klerk',
       'hirt', 'greene', 'ide', 'hans_stuck', 'mitter', 'flaherty',
       'chiesa', 'herrmann', 'ratzenberger', 'tingle', 'garrett',
       'leston', 'edwards', 'walter', 'niday', 'hesnault', 'hoyt',
       'homeier', 'mcwithey', 'constantine', 'dinsmore', 'charlton',
       'rahal', 'frere', 'macklin', 'bianchi', 'vukovich', 'ball',
       'john_james', 'williams', 'ernesto_brambilla', 'miller', 'neve',
       'ashdown', 'goldsmith', 'driver', 'davies', 'lovely', 'lawrence',
       'yoong', 'villota', 'marr', 'marsh', 'lennep', 'bruni',
       'magnussen', 'foyt', 'vaccarella', 'martin', 'rothengatter',
       'hobbs', 'collomb', 'volonterio', 'sharp', 'barilla', 'amati',
       'puzey', 'leoni', 'cade', 'vic_wilson', 'raby', 'peters',
       'christie', 'connor', 'allison', 'lippi', 'levegh', 'lewis-evans',
       'ramos', 'adams', 'guy_mairesse', 'leclere', 'branca', 'cantrell',
       'bucknum', 'anderson', 'ashmore', 'birger', 'follmer',
       'bussinello', 'terra', 'klenk', 'walker', 'john_barber', 'noda',
       'parsons', 'deletraz', 'belso', 'lagorce', 'hanks', 'rol',
       'charrington', 'johnstone', 'swaters', 'hellings', 'taramazzo',
       'flockhart', 'bristow', 'shawe_taylor', 'nalon', 'mccoy',
       'mike_taylor', 'testut', 'henry_taylor', 'colombo', 'bourdais',
       'bucci', 'firman', 'daywalt', 'emery', 'keller', 'unser', 'gerard',
       'fontes', 'toshio_suzuki', 'iglesias', 'munaron',
       'pietro_fittipaldi', 'zorzi', 'ongais', 'keizan', 'lang', 'kiesa',
       'schuppan', 'nicholson', 'obrien', 'morgan', 'armi', 'thompson',
       'bonomi', 'templeman', 'davis', 'goethals', 'peter_walker',
       'cogan', 'kling', 'cabral', 'slotemaker', 'hart', 'larrousse',
       'baumgartner', 'starrabba', 'bob_scott', 'mccarthy', 'laurent',
       'veith', 'sweikert', 'magee', 'hahne', 'trimmer', 'apicella',
       'legat', 'crawford', 'fry', 'dolhem', 'blanchard', 'barth',
       'herman', 'vos', 'guerra', 'clapham', 'may', 'estefano', 'karch',
       'seiffert', 'andrews', 'solana', 'rossi', 'tomaso', 'carini',
       'crook', 'evans', 'vyver', 'bayol', 'chamberlain', 'bechem',
       'montagny', 'rooyen', 'williamson', 'jean', 'georges_berger',
       'pilette', 'ryan', 'pagani', 'webb', 'seidel', 'robarts', 'Cannoc',
       'pollet', 'george_connor', 'holland', 'abecassis', 'friesacher',
       'pease', 'vonlanthen', 'gubby', 'owen', 'zunino', 'gartner',
       'brack', 'thackwell', 'jo_schlesser', 'grim', 'jover', 'francia',
       'sanesi', 'andre_pilette', 'halford', 'dochnal', 'bueb',
       'duncan_hamilton', 'james', 'pieterse', 'lotterer', 'doohan',
       'griffith', 'nelleman', 'hurtubise', 'kennedy']
constructor_options = ['mclaren', 'maserati', 'haas', 'eurobrun', 'parnelli', 'sauber',
       'mercedes', 'team_lotus', 'onyx', 'jordan', 'dallara', 'ligier',
       'red_bull', 'toro_rosso', 'ats', 'penske', 'toleman', 'prost',
       'renault', 'larrousse', 'alfa', 'force_india', 'march', 'bellasi',
       'cooper-climax', 'lesovsky', 'ferrari', 'brm', 'minardi',
       'tyrrell', 'brabham-brm', 'williams', 'benetton', 'lotus_racing',
       'brabham-repco', 'stewart', 'alpine', 'zakspeed', 'hwm',
       'caterham', 'arrows', 'coloni', 'aston_martin', 'behra-porsche',
       'theodore', 'bmw_sauber', 'surtees', 'ensign', 'jaguar', 'brabham',
       'hesketh', 'fittipaldi', 'alphatauri', 'mclaren-alfa_romeo',
       'toyota', 'racing_point', 'rb', 'bar', 'veritas', 'super_aguri',
       'shadow-ford', 'kuzma', 'footwork', 'scirocco', 'marussia',
       'lotus_f1', 'ram', 'gordini', 'vanwall', 'lola', 'porsche',
       'watson', 'lago', 'mclaren-ford', 'brawn', 'virgin', 'pacific',
       'leyton', 'brabham-ford', 'life', 'lotus-climax', 'emeryson',
       'lambo', 'hrt', 'kurtis_kraft', 'osella', 'phillips', 'shadow',
       'brabham-alfa_romeo', 'connaught', 'matra', 'lotus-brm',
       'cooper-maserati', 'simtek', 'honda', 'wolf', 'lotus-ford',
       'march-alfa_romeo', 'brabham-climax', 'iso_marlboro', 'spirit',
       'merzario', 'march-ford', 'moda', 'wetteroth', 'cooper', 'mf1',
       'fondmetal', 'ags', 'cisitalia', 'manor', 'matra-ford', 'forti',
       'rial', 'tecno', 'simca', 'spyker_mf1', 'martini', 'snowberger',
       'hill', 'cooper-brm', 'lec', 'epperly', 'osca', 'maki', 'trojan',
       'tomaso', 'mclaren-brm', 'eagle-weslake', 'lds-climax',
       'eagle-climax', 'spyker', 'bromme', 'schroeder', 'era', 'marchese',
       'jbw', 'vhristensen', 'gilby', 'lds-alfa_romeo', 'boro',
       'cooper-borgward', 'milano', 'cooper-ferrari', 'amon', 'fry',
       'brp', 'de_tomaso-osca', 'alta', 'deidt', 'adams',
       'de_tomaso-alfa_romeo', 'pawl', 'butterworth', 'stevens',
       'nichels', 'cooper-castellotti', 'lyncar', 'lds', 'protos',
       'lancia', 'lotus-maserati', 'moore', 'stebro', 'scarab',
       'cooper-osca', 'afm', 'pankratz', 'enb', 'trevis', 'emw',
       'sherman', 'meskowski', 'token']
circuit_options = ['hungaroring', 'long_beach', 'nurburgring', 'red_bull_ring',
       'monza', 'monaco', 'watkins_glen', 'villeneuve', 'galvez',
       'adelaide', 'suzuka', 'phoenix', 'americas', 'spa', 'brands_hatch',
       'catalunya', 'silverstone', 'jarama', 'kyalami', 'estoril',
       'hockenheimring', 'imola', 'bremgarten', 'charade', 'rodriguez',
       'indianapolis', 'zolder', 'interlagos', 'ricard', 'zeltweg',
       'marina_bay', 'albert_park', 'mosport', 'shanghai', 'yas_marina',
       'sepang', 'istanbul', 'miami', 'donington', 'zandvoort', 'bahrain',
       'anderstorp', 'fuji', 'jeddah', 'portimao', 'vegas', 'jacarepagua',
       'montjuic', 'baku', 'essarts', 'magny_cours', 'detroit', 'pescara',
       'jerez', 'valencia', 'buddh', 'sochi', 'reims', 'yeongam', 'dijon',
       'las_vegas', 'aintree', 'losail', 'mugello', 'george', 'riverside',
       'pedralbes', 'ain-diab', 'lemans', 'tremblant', 'nivelles',
       'sebring', 'okayama', 'boavista', 'dallas', 'avus', 'monsanto']
region_options = [0,1,2,3,4]

st.header("Enter Race Details")

col1, col2 = st.columns(2)

with col1:
    driverRef = st.selectbox("Driver", driver_options)
    constructorRef = st.selectbox("Constructor", constructor_options)
    circuitRef = st.selectbox("Circuit", circuit_options)
    circuit_region = st.selectbox("Circuit Region", region_options)
    grid = st.number_input("Grid Position (1–20)", min_value=1, max_value=20, step=1)
    round_no = st.number_input("Race Round", min_value=1, max_value=25, step=1)

with col2:
    race_date = st.date_input(
    "Race Date",
    value=datetime.date(2024, 3, 1),             # default value
    min_value=datetime.date(1900, 1, 1),         # allow selecting from 1900
    max_value=datetime.date(2100, 12, 31)        # optional, restrict future years
    )
    laps = st.number_input("Laps Completed", min_value=0, max_value=80, step=1)
    points = st.number_input("Points Earned", min_value=0.0, max_value=50.0, step=0.5)
    age_at_race = st.number_input("Driver Age at Race", min_value=17.0, max_value=70.0, step=1.0)

# Auto-generate derived date features
race_year = race_date.year
race_month = race_date.month
race_dayofweek = race_date.weekday()  # 0 = Monday, 6 = Sunday

# Add 'year' and 'positionOrder' logically
year = race_year
positionOrder = grid  # often similar in meaning for prediction

# Build input DataFrame exactly matching training columns
input_data = pd.DataFrame([{
    "year": year,
    "round": round_no,
    "grid": grid,
    "positionOrder": positionOrder,
    "points": points,
    "laps": laps,
    "age_at_race": age_at_race,
    "circuit_region": circuit_region,
    "race_year": race_year,
    "race_month": race_month,
    "race_dayofweek": race_dayofweek,
    "driverRef": driverRef,
    "constructorRef": constructorRef,
    "circuitRef": circuitRef
}])

# Show preview
st.subheader("🧾 Input Summary")
st.dataframe(input_data)

# --- Prediction ---
if st.button("Predict Finish Position"):
    try:
        prediction = model.predict(input_data)[0]
        if prediction ==0:
            st.error(" The model predicts that you won't finish the race")
        if prediction ==1:
            st.success(f" The model predicts that you will finish the race ")
    except Exception as e:
        st.error(f" Error during prediction: {e}")
