import random
import asyncio

countries = {
    "afghanistan":
        {
            "name": "Afghanistan",
            "capital": "Kabul",
            "geoguessr": "n",
        },
    "albania":
        {
            "name": "Albania",
            "capital": "Tirana",
            "geoguessr": "y",
        },
    "algeria":
        {
            "name": "Algeria",
            "capital": "Algiers",
            "geoguessr": "n",
        },
    "andorra":
        {
            "name": "Andorra",
            "capital": "Andorra la Vella",
            "geoguessr": "y",
        },
    "angola":
        {
            "name": "Angola",
            "capital": "Luanda",
            "geoguessr": "n",
        },
    "antigua and barbuda":
        {
            "name": "Antigua and Barbuda",
            "capital": "Saint John's",
            "geoguessr": "n",
        },
    "argentina":
        {
            "name": "Argentina",
            "capital": "Buenos Aires",
            "geoguessr": "y",
        },
    "armenia":
        {
            "name": "Armenia",
            "capital": "Yerevan",
            "geoguessr": "n",
        },
    "australia":
        {
            "name": "Australia",
            "capital": "Canberra",
            "geoguessr": "y",
        },
    "austria":
        {
            "name": "Austria",
            "capital": "Vienna",
            "geoguessr": "y",
        },
    "azerbaijan":
        {
            "name": "Azerbaijan",
            "capital": "Baku",
            "geoguessr": "n",
        },
    "bahamas":
        {
            "name": "Bahamas",
            "capital": "Nassau",
            "geoguessr": "n",
        },
    "bahrain":
        {
            "name": "Bahrain",
            "capital": "Manama",
            "geoguessr": "n",
        },
    "bangladesh":
        {
            "name": "Bangladesh",
            "capital": "Dhaka",
            "geoguessr": "y",
        },
    "barbados":
        {
            "name": "Barbados",
            "capital": "Bridgetown",
            "geoguessr": "n",
        },
    "belarus":
        {
            "name": "Belarus",
            "capital": "Minsk",
            "geoguessr": "n",
        },
    "belgium":
        {
            "name": "Belgium",
            "capital": "Brussels",
            "geoguessr": "y",
        },
    "belize":
        {
            "name": "Belize",
            "capital": "Belmopan",
            "geoguessr": "n",
        },
    "benin":
        {
            "name": "Benin",
            "capital": "Porto Novo",
            "geoguessr": "n",
        },
    "bhutan":
        {
            "name": "Bhutan",
            "capital": "Thimphu",
            "geoguessr": "y",
        },
    "bolivia":
        {
            "name": "Bolivia",
            "capital": "La Paz",
            "geoguessr": "y",
        },
    "bosnia and herzegovina":
        {
            "name": "Bosnia and Herzegovina",
            "capital": "Sarajevo",
            "geoguessr": "y",
        },
    "botswana":
        {
            "name": "Botswana",
            "capital": "Gaborone",
            "geoguessr": "y",
        },
    "brazil":
        {
            "name": "Brazil",
            "capital": "Brasilia",
            "geoguessr": "y",
        },
    "brunei":
        {
            "name": "Brunei",
            "capital": "Bandar Seri Begawan",
            "geoguessr": "n",
        },
    "bulgaria":
        {
            "name": "Bulgaria",
            "capital": "Sofia",
            "geoguessr": "y",
        },
    "burkina faso":
        {
            "name": "Burkina Faso",
            "capital": "Ouagadougou",
            "geoguessr": "n",
        },
    "burundi":
        {
            "name": "Burundi",
            "capital": "Gitega",
            "geoguessr": "n",
        },
    "cambodia":
        {
            "name": "Cambodia",
            "capital": "Phnom Penh",
            "geoguessr": "y",
        },
    "cameroon":
        {
            "name": "Cameroon",
            "capital": "Yaounde",
            "geoguessr": "n",
        },
    "canada":
        {
            "name": "Canada",
            "capital": "Ottawa",
            "geoguessr": "y",
        },
    "cape verde":
        {
            "name": "Cape Verde",
            "capital": "Praia",
            "geoguessr": "n",
        },
    "central african republic":
        {
            "name": "Central African Republic",
            "capital": "Bangui",
            "geoguessr": "n",
        },
    "chad":
        {
            "name": "Chad",
            "capital": "N'Djamena",
            "geoguessr": "n",
        },
    "chile":
        {
            "name": "Chile",
            "capital": "Santiago",
            "geoguessr": "y",
        },
    "china":
        {
            "name": "China",
            "capital": "Beijing",
            "geoguessr": "n",
        },
    "colombia":
        {
            "name": "Colombia",
            "capital": "Bogota",
            "geoguessr": "y",
        },
    "comoros":
        {
            "name": "Comoros",
            "capital": "Moroni",
            "geoguessr": "n",
        },
    "republic of the congo":
        {
            "name": "Republic of the Congo",
            "capital": "Kinshasa",
            "geoguessr": "n",
        },
    "democratic republic of the congo":
        {
            "name": "Democratic Republic of the Congo",
            "capital": "Brazzaville",
            "geoguessr": "n",
        },
    "costa rica":
        {
            "name": "Costa Rica",
            "capital": "San Jose",
            "geoguessr": "y",
        },
    "ivory coast":
        {
            "name": "Ivory Coast",
            "capital": "Yamoussoukro",
            "geoguessr": "n",
        },
    "croatia":
        {
            "name": "Croatia",
            "capital": "Zagreb",
            "geoguessr": "y",
        },
    "cuba":
        {
            "name": "Cuba",
            "capital": "Havana",
            "geoguessr": "n",
        },
    "cyprus":
        {
            "name": "Cyprus",
            "capital": "Nicosia",
            "geoguessr": "y",
        },
    "czechia":
        {
            "name": "Czechia",
            "capital": "Prague",
            "geoguessr": "y",
        },
    "denmark":
        {
            "name": "Denmark",
            "capital": "Copenhagen",
            "geoguessr": "y",
        },
    "djibouti":
        {
            "name": "Djibouti",
            "capital": "Djibouti",
            "geoguessr": "n",
        },
    "dominica":
        {
            "name": "Dominica",
            "capital": "Roseau",
            "geoguessr": "n",
        },
    "dominican republic":
        {
            "name": "Dominican Republic",
            "capital": "Santo Domingo",
            "geoguessr": "y",
        },
    "east timor":
        {
            "name": "East Timor",
            "capital": "Dili",
            "geoguessr": "n",
        },
    "ecuador":
        {
            "name": "Ecuador",
            "capital": "Quito",
            "geoguessr": "y",
        },
    "egypt":
        {
            "name": "Egypt",
            "capital": "Cairo",
            "geoguessr": "n",
        },
    "el salvador":
        {
            "name": "El Salvador",
            "capital": "San Salvador",
            "geoguessr": "n",
        },
    "england":
        {
            "name": "England",
            "capital": "London",
            "geoguessr": "y",
        },
    "equatorial guinea":
        {
            "name": "Equatorial Guinea",
            "capital": "Ciudad de la Paz",
            "geoguessr": "n",
        },
    "eritrea":
        {
            "name": "Eritrea",
            "capital": "Asmara",
            "geoguessr": "n",
        },
    "estonia":
        {
            "name": "Estonia",
            "capital": "Tallinn",
            "geoguessr": "y",
        },
    "eswatini":
        {
            "name": "Eswatini",
            "capital": "Mbabane",
            "geoguessr": "y",
        },
    "ethiopia":
        {
            "name": "Ethiopia",
            "capital": "Addis Ababa",
            "geoguessr": "n",
        },
    "federated states of micronesia":
        {
            "name": "Federated States of Micronesia",
            "capital": "Palikir",
            "geoguessr": "n",
        },
    "fiji":
        {
            "name": "Fiji",
            "capital": "Suva",
            "geoguessr": "n",
        },
    "finland":
        {
            "name": "Finland",
            "capital": "Helsinki",
            "geoguessr": "y",
        },
    "france":
        {
            "name": "France",
            "capital": "Paris",
            "geoguessr": "y",
        },
    "gabon":
        {
            "name": "Gabon",
            "capital": "Libreville",
            "geoguessr": "n",
        },
    "gambia":
        {
            "name": "Gambia",
            "capital": "Banjul",
            "geoguessr": "n",
        },
    "georgia":
        {
            "name": "Georgia",
            "capital": "Tbilisi",
            "geoguessr": "n",
        },
    "germany":
        {
            "name": "Germany",
            "capital": "Berlin",
            "geoguessr": "y",
        },
    "ghana":
        {
            "name": "Ghana",
            "capital": "Accra",
            "geoguessr": "y",
        },
    "greece":
        {
            "name": "Greece",
            "capital": "Athens",
            "geoguessr": "y",
        },
    "grenada":
        {
            "name": "Grenada",
            "capital": "Saint George's",
            "geoguessr": "n",
        },
    "guatemala":
        {
            "name": "Guatemala",
            "capital": "Guatemala City",
            "geoguessr": "y",
        },
    "guinea":
        {
            "name": "Guinea",
            "capital": "Conakry",
            "geoguessr": "n",
        },
    "guinea-bissau":
        {
            "name": "Guinea-Bissau",
            "capital": "Bissau",
            "geoguessr": "n",
        },
    "guyana":
        {
            "name": "Guyana",
            "capital": "Georgetown",
            "geoguessr": "n",
        },
    "haiti":
        {
            "name": "Haiti",
            "capital": "Port au Prince",
            "geoguessr": "n",
        },
    "honduras":
        {
            "name": "Honduras",
            "capital": "Tegucigalpa",
            "geoguessr": "n",
        },
    "hungary":
        {
            "name": "Hungary",
            "capital": "Budapest",
            "geoguessr": "y",
        },
    "iceland":
        {
            "name": "Iceland",
            "capital": "Reykjavik",
            "geoguessr": "y",
        },
    "india":
        {
            "name": "India",
            "capital": "New Delhi",
            "geoguessr": "y",
        },
    "indonesia":
        {
            "name": "Indonesia",
            "capital": "Jakarta",
            "geoguessr": "y",
        },
    "iran":
        {
            "name": "Iran",
            "capital": "Tehran",
            "geoguessr": "n",
        },
    "iraq":
        {
            "name": "Iraq",
            "capital": "Baghdad",
            "geoguessr": "n",
        },
    "ireland":
        {
            "name": "Ireland",
            "capital": "Dublin",
            "geoguessr": "y",
        },
    "israel":
        {
            "name": "Israel",
            "capital": "Jerusalem",
            "geoguessr": "y",
        },
    "italy":
        {
            "name": "Italy",
            "capital": "Rome",
            "geoguessr": "y",
        },
    "jamaica":
        {
            "name": "Jamaica",
            "capital": "Kingston",
            "geoguessr": "n",
        },
    "japan":
        {
            "name": "Japan",
            "capital": "Tokyo",
            "geoguessr": "y",
        },
    "jordan":
        {
            "name": "Jordan",
            "capital": "Amman",
            "geoguessr": "y",
        },
    "kazakhstan":
        {
            "name": "Kazakhstan",
            "capital": "Astana",
            "geoguessr": "y",
        },
    "kenya":
        {
            "name": "Kenya",
            "capital": "Nairobi",
            "geoguessr": "y",
        },
    "kiribati":
        {
            "name": "Kiribati",
            "capital": "Tarawa Atoll",
            "geoguessr": "n",
        },
    "kosovo":
        {
            "name": "Kosovo",
            "capital": "Pristina",
            "geoguessr": "n",
        },
    "kuwait":
        {
            "name": "Kuwait",
            "capital": "Kuwait City",
            "geoguessr": "n",
        },
    "kyrgyzstan":
        {
            "name": "Kyrgyzstan",
            "capital": "Bishkek",
            "geoguessr": "y",
        },
    "laos":
        {
            "name": "Laos",
            "capital": "Vientiane",
            "geoguessr": "y",
        },
    "latvia":
        {
            "name": "Latvia",
            "capital": "Riga",
            "geoguessr": "y",
        },
    "lebanon":
        {
            "name": "Lebanon",
            "capital": "Beirut",
            "geoguessr": "n",
        },
    "lesotho":
        {
            "name": "Lesotho",
            "capital": "Maseru",
            "geoguessr": "y",
        },
    "liberia":
        {
            "name": "Liberia",
            "capital": "Monrovia",
            "geoguessr": "n",
        },
    "libya":
        {
            "name": "Libya",
            "capital": "Tripoli",
            "geoguessr": "n",
        },
    "liechtenstein":
        {
            "name": "Liechtenstein",
            "capital": "Vaduz",
            "geoguessr": "y",
        },
    "lithuania":
        {
            "name": "Lithuania",
            "capital": "Vilnius",
            "geoguessr": "y",
        },
    "luxembourg":
        {
            "name": "Luxembourg",
            "capital": "Luxembourg",
            "geoguessr": "y",
        },
    "madagascar":
        {
            "name": "Madagascar",
            "capital": "Antananarivo",
            "geoguessr": "y",
        },
    "malawi":
        {
            "name": "Malawi",
            "capital": "Lilongwe",
            "geoguessr": "n",
        },
    "malaysia":
        {
            "name": "Malaysia",
            "capital": "Kuala Lumpur",
            "geoguessr": "y",
        },
    "maldives":
        {
            "name": "Maldives",
            "capital": "Male",
            "geoguessr": "n",
        },
    "mali":
        {
            "name": "Mali",
            "capital": "Bamako",
            "geoguessr": "n",
        },
    "malta":
        {
            "name": "Malta",
            "capital": "Valletta",
            "geoguessr": "y",
        },
    "marshall islands":
        {
            "name": "Marshall Islands",
            "capital": "Majuro",
            "geoguessr": "n",
        },
    "mauritania":
        {
            "name": "Mauritania",
            "capital": "Nouakchott",
            "geoguessr": "n",
        },
    "mauritius":
        {
            "name": "Mauritius",
            "capital": "Port Louis",
            "geoguessr": "n",
        },
    "mexico":
        {
            "name": "Mexico",
            "capital": "Mexico City",
            "geoguessr": "y",
        },
    "moldova":
        {
            "name": "Moldova",
            "capital": "Chisinau",
            "geoguessr": "n",
        },
    "monaco":
        {
            "name": "Monaco",
            "capital": "Monaco",
            "geoguessr": "y",
        },
    "mongolia":
        {
            "name": "Mongolia",
            "capital": "Ulaanbaatar",
            "geoguessr": "y",
        },
    "montenegro":
        {
            "name": "Montenegro",
            "capital": "Podgorica",
            "geoguessr": "y",
        },
    "morocco":
        {
            "name": "Morocco",
            "capital": "Rabat",
            "geoguessr": "n",
        },
    "mozambique":
        {
            "name": "Mozambique",
            "capital": "Maputo",
            "geoguessr": "n",
        },
    "myanmar (burma)":
        {
            "name": "Myanmar (Burma)",
            "capital": "Nay Pyi Taw",
            "geoguessr": "n",
        },
    "namibia":
        {
            "name": "Namibia",
            "capital": "Windhoek",
            "geoguessr": "y",
        },
    "nauru":
        {
            "name": "Nauru",
            "capital": "None",
            "geoguessr": "n",
        },
    "nepal":
        {
            "name": "Nepal",
            "capital": "Kathmandu",
            "geoguessr": "n",
        },
    "netherlands":
        {
            "name": "Netherlands",
            "capital": "Amsterdam",
            "geoguessr": "y",
        },
    "new zealand":
        {
            "name": "New Zealand",
            "capital": "Wellington",
            "geoguessr": "y",
        },
    "nicaragua":
        {
            "name": "Nicaragua",
            "capital": "Managua",
            "geoguessr": "n",
        },
    "niger":
        {
            "name": "Niger",
            "capital": "Niamey",
            "geoguessr": "n",
        },
    "nigeria":
        {
            "name": "Nigeria",
            "capital": "Abuja",
            "geoguessr": "y",
        },
    "north korea":
        {
            "name": "North Korea",
            "capital": "Pyongyang",
            "geoguessr": "n",
        },
    "north macedonia":
        {
            "name": "North Macedonia",
            "capital": "Skopje",
            "geoguessr": "y",
        },
    "northern ireland":
        {
            "name": "Northern Ireland",
            "capital": "Belfast",
            "geoguessr": "y",
        },
    "norway":
        {
            "name": "Norway",
            "capital": "Oslo",
            "geoguessr": "y",
        },
    "oman":
        {
            "name": "Oman",
            "capital": "Muscat",
            "geoguessr": "y",
        },
    "pakistan":
        {
            "name": "Pakistan",
            "capital": "Islamabad",
            "geoguessr": "n",
        },
    "palau":
        {
            "name": "Palau",
            "capital": "Ngerulmud",
            "geoguessr": "n",
        },
    "palestine":
        {
            "name": "Palestine",
            "capital": "Jerusalem",
            "geoguessr": "y",
        },
    "panama":
        {
            "name": "Panama",
            "capital": "Panama City",
            "geoguessr": "y",
        },
    "papua new guinea":
        {
            "name": "Papua New Guinea",
            "capital": "Port Moresby",
            "geoguessr": "n",
        },
    "paraguay":
        {
            "name": "Paraguay",
            "capital": "Asuncion",
            "geoguessr": "y",
        },
    "peru":
        {
            "name": "Peru",
            "capital": "Lima",
            "geoguessr": "y",
        },
    "philippines":
        {
            "name": "Philippines",
            "capital": "Manila",
            "geoguessr": "y",
        },
    "poland":
        {
            "name": "Poland",
            "capital": "Warsaw",
            "geoguessr": "y",
        },
    "portugal":
        {
            "name": "Portugal",
            "capital": "Lisbon",
            "geoguessr": "y",
        },
    "qatar":
        {
            "name": "Qatar",
            "capital": "Doha",
            "geoguessr": "y",
        },
    "romania":
        {
            "name": "Romania",
            "capital": "Bucharest",
            "geoguessr": "y",
        },
    "russia":
        {
            "name": "Russia",
            "capital": "Moscow",
            "geoguessr": "y",
        },
    "rwanda":
        {
            "name": "Rwanda",
            "capital": "Kigali",
            "geoguessr": "y",
        },
    "saint kitts and nevis":
        {
            "name": "Saint Kitts and Nevis",
            "capital": "Basseterre",
            "geoguessr": "n",
        },
    "saint lucia":
        {
            "name": "Saint Lucia",
            "capital": "Castries",
            "geoguessr": "n",
        },
    "saint vincent and the grenadines":
        {
            "name": "Saint Vincent and the Grenadines",
            "capital": "Kingstown",
            "geoguessr": "n",
        },
    "samoa":
        {
            "name": "Samoa",
            "capital": "Apia",
            "geoguessr": "y",
        },
    "san marino":
        {
            "name": "San Marino",
            "capital": "San Marino",
            "geoguessr": "y",
        },
    "sao tome and principe":
        {
            "name": "Sao Tome and Principe",
            "capital": "Sao Tome",
            "geoguessr": "n",
        },
    "saudi arabia":
        {
            "name": "Saudi Arabia",
            "capital": "Riyadh",
            "geoguessr": "n",
        },
    "scotland":
        {
            "name": "Scotland",
            "capital": "Edinburgh",
            "geoguessr": "y",
        },
    "senegal":
        {
            "name": "Senegal",
            "capital": "Dakar",
            "geoguessr": "y",
        },
    "serbia":
        {
            "name": "Serbia",
            "capital": "Belgrade",
            "geoguessr": "y",
        },
    "seychelles":
        {
            "name": "Seychelles",
            "capital": "Victoria",
            "geoguessr": "n",
        },
    "sierra leone":
        {
            "name": "Sierra Leone",
            "capital": "Freetown",
            "geoguessr": "n",
        },
    "singapore":
        {
            "name": "Singapore",
            "capital": "Singapore",
            "geoguessr": "y",
        },
    "slovakia":
        {
            "name": "Slovakia",
            "capital": "Bratislava",
            "geoguessr": "y",
        },
    "slovenia":
        {
            "name": "Slovenia",
            "capital": "Ljubljana",
            "geoguessr": "y",
        },
    "solomon islands":
        {
            "name": "Solomon Islands",
            "capital": "Honiara",
            "geoguessr": "n",
        },
    "somalia":
        {
            "name": "Somalia",
            "capital": "Mogadishu",
            "geoguessr": "n",
        },
    "south africa":
        {
            "name": "South Africa",
            "capital": "Pretoria, Cape Town, Bloemfontein",
            "geoguessr": "y",
        },
    "south korea":
        {
            "name": "South Korea",
            "capital": "Seoul",
            "geoguessr": "y",
        },
    "south sudan":
        {
            "name": "South Sudan",
            "capital": "Juba",
            "geoguessr": "n",
        },
    "spain":
        {
            "name": "Spain",
            "capital": "Madrid",
            "geoguessr": "y",
        },
    "sri lanka":
        {
            "name": "Sri Lanka",
            "capital": "Sri Jayawardenpura Kotte",
            "geoguessr": "y",
        },
    "sudan":
        {
            "name": "Sudan",
            "capital": "Khartoum",
            "geoguessr": "n",
        },
    "suriname":
        {
            "name": "Suriname",
            "capital": "Paramaribo",
            "geoguessr": "n",
        },
    "sweden":
        {
            "name": "Sweden",
            "capital": "Stockholm",
            "geoguessr": "y",
        },
    "switzerland":
        {
            "name": "Switzerland",
            "capital": "Bern",
            "geoguessr": "y",
        },
    "syria":
        {
            "name": "Syria",
            "capital": "Damascus",
            "geoguessr": "n",
        },
    "taiwan":
        {
            "name": "Taiwan",
            "capital": "Taipei",
            "geoguessr": "y",
        },
    "tajikistan":
        {
            "name": "Tajikistan",
            "capital": "Dushanbe",
            "geoguessr": "n",
        },
    "tanzania":
        {
            "name": "Tanzania",
            "capital": "Dodoma",
            "geoguessr": "n",
        },
    "thailand":
        {
            "name": "Thailand",
            "capital": "Bangkok",
            "geoguessr": "y",
        },
    "togo":
        {
            "name": "Togo",
            "capital": "Lome",
            "geoguessr": "n",
        },
    "tonga":
        {
            "name": "Tonga",
            "capital": "Nuku'alofa",
            "geoguessr": "n",
        },
    "trinidad and tobago":
        {
            "name": "Trinidad and Tobago",
            "capital": "Port of Spain",
            "geoguessr": "n",
        },
    "tunisia":
        {
            "name": "Tunisia",
            "capital": "Tunis",
            "geoguessr": "y",
        },
    "turkiye":
        {
            "name": "Turkiye",
            "capital": "Ankara",
            "geoguessr": "y",
        },
    "turkmenistan":
        {
            "name": "Turkmenistan",
            "capital": "Ashgabat",
            "geoguessr": "n",
        },
    "tuvalu":
        {
            "name": "Tuvalu",
            "capital": "Funafuti",
            "geoguessr": "n",
        },
    "uganda":
        {
            "name": "Uganda",
            "capital": "Kampala",
            "geoguessr": "y",
        },
    "ukraine":
        {
            "name": "Ukraine",
            "capital": "Kyiv",
            "geoguessr": "y",
        },
    "united arab emirates":
        {
            "name": "United Arab Emirates",
            "capital": "Abu Dhabi",
            "geoguessr": "y",
        },
    "united kingdom":
        {
            "name": "United Kingdom",
            "capital": "London",
            "geoguessr": "y",
        },
    "united states":
        {
            "name": "United States",
            "capital": "Washington DC",
            "geoguessr": "y",
        },
    "uruguay":
        {
            "name": "Uruguay",
            "capital": "Montevideo",
            "geoguessr": "y",
        },
    "uzbekistan":
        {
            "name": "Uzbekistan",
            "capital": "Tashkent",
            "geoguessr": "n",
        },
    "vanuatu":
        {
            "name": "Vanuatu",
            "capital": "Port Vila",
            "geoguessr": "n",
        },
    "vatican city":
        {
            "name": "Vatican City",
            "capital": "Caitcan City",
            "geoguessr": "y",
        },
    "venezuela":
        {
            "name": "Venezuela",
            "capital": "Caracas",
            "geoguessr": "n",
        },
    "vietnam":
        {
            "name": "Vietnam",
            "capital": "Hanoi",
            "geoguessr": "y",
        },
    "wales":
        {
            "name": "Wales",
            "capital": "Cardiff",
            "geoguessr": "y",
        },
    "yemen":
        {
            "name": "Yemen",
            "capital": "Sana'a",
            "geoguessr": "n",
        },
    "zambia":
        {
            "name": "Zambia",
            "capital": "Lusaka",
            "geoguessr": "n",
        },
    "zimbabwe":
        {
            "name": "Zimbabwe",
            "capital": "Harare",
            "geoguessr": "n",
        },
}