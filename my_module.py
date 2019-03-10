import pandas as pd
import requests
import zipfile
from glob import glob

african_countries = ['Angola', 'Burundi', 'Benin', 'Burkina Faso', 'Botswana', 'Central African Republic', 'Cote d\'Ivoire', 'Cameroon', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Comoros', 'Cabo Verde', 'Djibouti', 'Algeria', 'Egypt, Arab Rep.', 'Eritrea', 'Ethiopia', 'Gabon', 'Ghana', 'Guinea', 'Gambia, The', 'Guinea-Bissau', 'Equatorial Guinea', 'Kenya', 'Liberia', 'Libya', 'Lesotho', 'Morocco', 'Madagascar', 'Mali', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sudan', 'Senegal', 'Sierra Leone', 'Somalia', 'South Sudan', 'Sao Tome and Principe', 'Eswatini', 'Seychelles', 'Chad', 'Togo', 'Tanzania', 'Uganda', 'South Africa', 'Zambia', 'Zimbabwe']
asian_countries = ['Azerbaijan', 'Bangladesh', 'Brunei Darussalam', 'Bhutan', 'China', 'Hong Kong SAR, China', 'Indonesia', 'India', 'Japan', 'Kyrgyz Republic', 'Cambodia', 'Korea, Rep.', 'Lao PDR', 'Sri Lanka', 'Macao SAR, China', 'Maldives', 'Myanmar', 'Mongolia', 'Malaysia', 'Nepal', 'Philippines', 'Korea, Dem. People’s Rep.', 'Singapore', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Tunisia', 'Uzbekistan', 'Vietnam']
central_american_countries = ['Belize', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama']
central_american_caribbean_countries = ['Aruba', 'Antigua and Barbuda', 'Bahamas, The', 'Belize', 'Bermuda', 'Costa Rica', 'Cuba', 'Curacao', 'Cayman Islands', 'Dominica', 'Dominican Republic', 'Grenada', 'Guatemala', 'Honduras', 'Haiti', 'Jamaica', 'St. Kitts and Nevis', 'St. Lucia', 'St. Martin (French part)', 'Nicaragua', 'Panama', 'Puerto Rico', 'El Salvador', 'Sint Maarten', 'Trinidad and Tobago', 'St. Vincent and the Grenadines', 'British Virgin Islands', 'Virgin Islands (U.S.)']
european_countries = ['Albania', 'Andorra', 'Armenia', 'Austria', 'Belgium', 'Bulgaria', 'Bosnia and Herzegovina', 'Belarus', 'Switzerland', 'Cyprus', 'Czech Republic', 'Germany', 'Denmark', 'Spain', 'Estonia', 'Finland', 'France', 'Faroe Islands', 'United Kingdom', 'Georgia', 'Gibraltar', 'Greece', 'Croatia', 'Hungary', 'Ireland', 'Iceland', 'Italy', 'Kazakhstan', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Latvia', 'Monaco', 'Moldova', 'Macedonia', 'Malta', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'San Marino', 'Serbia', 'Slovak Republic', 'Slovenia', 'Sweden', 'Turkey', 'Ukraine', 'Kosovo']
middle_eastern_countries = ['Afghanistan', 'United Arab Emirates', 'Bahrain', 'Iran, Islamic Rep.', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Oman', 'Pakistan', 'Qatar', 'Saudi Arabia', 'Syrian Arab Republic', 'Yemen, Rep.']
north_american_countries = ['Canada', 'Greenland', 'Mexico', 'Turks and Caicos Islands', 'United States']
oceanian_countries = ['American Samoa', 'Australia', 'Fiji', 'Micronesia, Fed. Sts.', 'Guam', 'Kiribati', 'Marshall Islands', 'Northern Mariana Islands', 'New Caledonia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'French Polynesia', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu', 'Samoa']
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Barbados', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Peru', 'Paraguay', 'Suriname', 'Uruguay', 'Venezuela']

def get_dataframe_from_url(url):
    # downloading data
    response = requests.get(url)
    # extracting filename
    fname = response.headers['Content-Disposition'].split('=')[1]
    if response.ok:  # status_code == 200:
        # opens the file
        with open(fname, 'wb') as f:
            f.write(response.content)
    # unpacking zip
    zipfile.ZipFile(fname, 'r').extractall('.')
    # finding the file
    local_file = glob('./API*.csv')[0]
    # reads file, skips first 4 rows
    df = pd.read_csv(local_file,skiprows=4)
    return df