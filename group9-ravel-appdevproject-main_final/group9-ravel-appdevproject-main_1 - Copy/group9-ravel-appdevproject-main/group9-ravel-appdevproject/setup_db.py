import sqlite3

def create_database():
    conn = sqlite3.connect('ravel_database.db')
    cursor = conn.cursor()

    # 1. User Table (UPDATED with LinkedArtistID)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Email TEXT UNIQUE NOT NULL,
        Password TEXT NOT NULL,
        UserType TEXT,
        LinkedArtistID INTEGER
    )
    ''')

    # 2. Artist Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Artist (
        ArtistID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        StreamCount INTEGER,
        IsUnderrepresented BOOLEAN
    )
    ''')

    # 3. Track Table (UPDATED with FilePath)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Track (
        TrackID INTEGER PRIMARY KEY AUTOINCREMENT,
        ArtistID INTEGER,
        Title TEXT NOT NULL,
        Genre TEXT,
        PlayCount INTEGER,
        FilePath TEXT,
        FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
    )
    ''')

    # 4. Playlist Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Playlist (
        PlaylistID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        GeneratedTitle TEXT,
        DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID)
    )
    ''')

    # 5. Contains Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Contains (
        PlaylistID INTEGER,
        TrackID INTEGER,
        FOREIGN KEY (PlaylistID) REFERENCES Playlist(PlaylistID),
        FOREIGN KEY (TrackID) REFERENCES Track(TrackID)
    )
    ''')

    # 6. AI_Session Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS AI_Session (
        SessionID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        SessionNumber INTEGER,
        StartDate DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID)
    )
    ''')

    # 7. AI_Interaction Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS AI_Interaction (
        InteractionID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        SessionID INTEGER,
        Message TEXT,
        Role TEXT DEFAULT 'user',
        TimeStamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID),
        FOREIGN KEY (SessionID) REFERENCES AI_Session(SessionID)
    )
    ''')

    # 8. ListenHistory Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ListenHistory (
        HistoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        TrackID INTEGER,
        Genre TEXT,
        ListenedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID),
        FOREIGN KEY (TrackID) REFERENCES Track(TrackID)
    )
    ''')

    # 9. SearchHistory Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SearchHistory (
        HistoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        ResultName TEXT,
        ResultType TEXT,
        ResultID INTEGER,
        Genre TEXT,
        ArtistName TEXT,
        SearchedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID)
    )
    ''')

    # --- INSERT DUMMY DATA FOR TESTING ---
    cursor.execute("DELETE FROM Artist")
    cursor.execute("DELETE FROM Track")
    cursor.execute("DELETE FROM Contains")
    cursor.execute("DELETE FROM ListenHistory")
    for tbl in ('Artist', 'Track'):
        try:
            cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{tbl}'")
        except Exception:
            pass

    artists = [
        ('The Weeknd',           500000000, False),
        ('Taylor Swift',         800000000, False),
        ('Drake',                750000000, False),
        ('Billie Eilish',        600000000, False),
        ('Ed Sheeran',           700000000, False),
        ('Kendrick Lamar',       450000000, False),
        ('Beyonce',              650000000, False),
        ('Bruno Mars',           400000000, False),
        ('Doja Cat',             380000000, False),
        ('Harry Styles',         350000000, False),
        ('Bad Bunny',            500000000, False),
        ('Post Malone',          420000000, False),
        ('Ariana Grande',        600000000, False),
        ('Imagine Dragons',      300000000, False),
        ('Coldplay',             550000000, False),
        ('Eminem',               480000000, False),
        ('Rihanna',              600000000, False),
        ('SZA',                  280000000, False),
        ('Tyler, the Creator',   300000000, False),
        ('Frank Ocean',          200000000, False),
        ('Local Indie Band A',         850,  True),
        ('Underground Synth Project',  300,  True),
        ('New Acoustic Guy',           150,  True),
        ('Ben&Ben',                   5000,  True),
        ('IV of Spades',              3000,  True),
        ('December Avenue',           4000,  True),
        ('Cup of Joe',                2000,  True),
        ('Lola Amour',                1500,  True),
        ('Moonstar88',                6000,  True),
        ('Hale',                      5500,  True),
        ('Urbandub',                  4500,  True),
        ('Phoebe Bridgers',           8000,  True),
        ('Mitski',                    9000,  True),
        ('Japanese Breakfast',        7000,  True),
        ('beabadoobee',               6000,  True),
        ('Cavetown',                  5000,  True),
        ('Wet Leg',                   4000,  True),
        ('Men I Trust',               3500,  True),
        ('Omar Apollo',               5500,  True),
        ('Remi Wolf',                 4200,  True),
        ('Snail Mail',                5000,  True),
        ('Soccer Mommy',              4800,  True),
        ('Big Thief',                 6000,  True),
        ('Novo Amor',                 8000,  True),
        ('Hollow Coves',              7000,  True),
        ('Clairo',                    9500,  True),
        ('Girl in Red',               9000,  True),
        ('Rex Orange County',         9200,  True),
        ('LANY',                      8500,  True),
        ('Cigarettes After Sex',       8000,  True),
    ]
    cursor.executemany('INSERT INTO Artist (Name, StreamCount, IsUnderrepresented) VALUES (?, ?, ?)', artists)

    tracks = [
        (1, 'Blinding Lights',        'Pop',       100000000),
        (1, 'Starboy',                'R&B',        90000000),
        (1, 'Save Your Tears',        'Pop',        85000000),
        (1, 'After Hours',            'R&B',        70000000),
        (1, 'Die For You',            'R&B',        60000000),
        (2, 'Cruel Summer',           'Pop',       150000000),
        (2, 'Anti-Hero',              'Pop',       200000000),
        (2, 'Style',                  'Pop',        80000000),
        (2, 'Love Story',             'Country',   120000000),
        (2, 'Shake It Off',           'Pop',       180000000),
        (3, "God's Plan",             'Hip-Hop',   160000000),
        (3, 'One Dance',              'R&B',       140000000),
        (3, 'Hotline Bling',          'Hip-Hop',   130000000),
        (3, 'Started From The Bottom','Hip-Hop',    90000000),
        (3, 'Passionfruit',           'R&B',        80000000),
        (4, 'Bad Guy',                'Pop',       200000000),
        (4, 'Happier Than Ever',       'Alternative',150000000),
        (4, 'Ocean Eyes',             'Pop',       120000000),
        (4, 'Therefore I Am',         'Pop',       100000000),
        (4, 'Lovely',                 'Alternative',130000000),
        (5, 'Shape of You',           'Pop',       300000000),
        (5, 'Perfect',                'Pop',       250000000),
        (5, 'Thinking Out Loud',      'Pop',       200000000),
        (5, 'Photograph',             'Folk',      180000000),
        (5, 'Castle on the Hill',     'Folk',      150000000),
        (6, 'HUMBLE.',                'Hip-Hop',   200000000),
        (6, 'Alright',                'Hip-Hop',   150000000),
        (6, 'Swimming Pools',         'Hip-Hop',   120000000),
        (6, 'Money Trees',            'Hip-Hop',   100000000),
        (6, 'DNA.',                   'Hip-Hop',   180000000),
        (7, 'Crazy in Love',          'R&B',       200000000),
        (7, 'Halo',                   'Pop',       180000000),
        (7, 'Formation',              'R&B',       150000000),
        (7, 'Single Ladies',          'Pop',       200000000),
        (7, 'Love On Top',            'R&B',       120000000),
        (8, 'Uptown Funk',            'Funk',      300000000),
        (8, 'Just the Way You Are',   'Pop',       200000000),
        (8, 'Grenade',                'Pop',       180000000),
        (8, '24K Magic',              'Funk',      150000000),
        (8, 'Locked Out of Heaven',   'Pop',       170000000),
        (9, 'Say So',                 'Pop',       150000000),
        (9, 'Kiss Me More',           'Pop',       130000000),
        (9, 'Need To Know',           'Hip-Hop',   100000000),
        (9, 'Woman',                  'Pop',        80000000),
        (10, 'Watermelon Sugar',      'Pop',       150000000),
        (10, 'As It Was',             'Pop',       200000000),
        (10, 'Golden',                'Pop',       130000000),
        (10, 'Adore You',             'Pop',       120000000),
        (10, 'Sign of the Times',     'Alternative',100000000),
        (11, 'Dakiti',                'Latin',     180000000),
        (11, 'Titi Me Pregunto',      'Latin',     150000000),
        (11, 'Yonaguni',              'Latin',     120000000),
        (11, 'Me Porto Bonito',       'Latin',     130000000),
        (12, 'Sunflower',             'Pop',       200000000),
        (12, 'Rockstar',              'Hip-Hop',   180000000),
        (12, 'Circles',               'Pop',       160000000),
        (12, 'Better Now',            'Pop',       150000000),
        (12, 'White Iverson',         'Hip-Hop',   100000000),
        (13, '7 Rings',               'Pop',       200000000),
        (13, 'Thank U, Next',         'Pop',       250000000),
        (13, 'Problem',               'Pop',       180000000),
        (13, 'Into You',              'Pop',       160000000),
        (13, 'God is a Woman',        'R&B',       140000000),
        (14, 'Believer',              'Alternative',200000000),
        (14, 'Radioactive',           'Alternative',250000000),
        (14, 'Thunder',               'Pop',       180000000),
        (14, 'Enemy',                 'Alternative',150000000),
        (14, 'Demons',                'Alternative',130000000),
        (15, 'Yellow',                'Alternative',200000000),
        (15, 'The Scientist',         'Alternative',180000000),
        (15, 'Fix You',               'Alternative',200000000),
        (15, 'Viva la Vida',          'Alternative',220000000),
        (15, 'A Sky Full of Stars',   'Pop',       150000000),
        (16, 'Lose Yourself',         'Hip-Hop',   300000000),
        (16, 'Not Afraid',            'Hip-Hop',   200000000),
        (16, 'Stan',                  'Hip-Hop',   180000000),
        (16, 'Without Me',            'Hip-Hop',   160000000),
        (16, 'Rap God',               'Hip-Hop',   150000000),
        (17, 'Umbrella',              'Pop',       200000000),
        (17, 'Diamonds',              'Pop',       220000000),
        (17, 'We Found Love',         'Pop',       250000000),
        (17, 'Stay',                  'R&B',       180000000),
        (17, 'Work',                  'R&B',       150000000),
        (18, 'Kill Bill',             'R&B',       150000000),
        (18, 'Snooze',                'R&B',       130000000),
        (18, 'Good Days',             'Alternative',120000000),
        (18, 'Love Galore',           'R&B',        90000000),
        (19, 'EARFQUAKE',             'R&B',       100000000),
        (19, 'See You Again',         'Alternative', 90000000),
        (19, "IGOR's Theme",          'Hip-Hop',    80000000),
        (19, 'Lumberjack',            'Hip-Hop',    70000000),
        (20, 'Thinking Bout You',     'R&B',       150000000),
        (20, 'Chanel',                'R&B',       100000000),
        (20, 'Ivy',                   'Alternative', 90000000),
        (20, 'Pink + White',          'R&B',       120000000),
        (20, 'Nights',                'Soul',       80000000),
        (21, 'Midnight Rain in Manila','Indie Rock',    500),
        (21, 'Wasted Youth',           'Indie Rock',    300),
        (21, 'Glass Walls',            'Alternative',   200),
        (22, 'Neon Dreams',            'Synthwave',     120),
        (22, 'Chrome City',            'Electronic',     90),
        (22, 'Signal Lost',            'Synthwave',      80),
        (23, 'Coffee Shop Acoustic',   'Acoustic',       80),
        (23, 'Morning Drive',          'Folk',           60),
        (23, 'Porch Light',            'Acoustic',       50),
        (24, 'Leaves',                 'OPM',          4500),
        (24, 'Maybe the Night',        'OPM',          5000),
        (24, 'Ride Home',              'Folk',         3000),
        (24, 'Pasalubong',             'OPM',          3500),
        (25, 'Where Have You Been My Disco','Funk',  2800),
        (25, 'Come Inside of My Heart', 'Pop',       2500),
        (25, 'Mundo',                  'OPM',          3000),
        (26, 'Bulong',                 'OPM',          3800),
        (26, 'Sa Ngalan ng Pag-ibig',  'OPM',          4000),
        (26, 'Huling Sandali',         'Alternative',  3200),
        (26, 'Kung Di Rin Lang Ikaw',  'OPM',          4500),
        (27, 'Paraluman',              'OPM',          1800),
        (27, 'Pag Inibig Kita',        'OPM',          2000),
        (27, 'Tsismosa',               'OPM',          1500),
        (28, 'Fallen',                 'OPM',          1400),
        (28, 'Staying',                'OPM',          1300),
        (28, 'Elysian',                'Pop',          1000),
        (29, 'Torete',                 'OPM',          5800),
        (29, 'Migraine',               'OPM',          5000),
        (29, 'Pangako',                'OPM',          4500),
        (30, 'The Day You Said Goodnight','OPM',      5200),
        (30, 'Blue Sky',               'Rock',         4800),
        (30, 'Broken Sonnet',          'Alternative',  4200),
        (31, 'Come',                   'OPM',          4200),
        (31, 'First of Summer',        'Rock',         3900),
        (31, 'The Fight Is Over',      'Alternative',  3500),
        (32, 'Motion Sickness',        'Indie Rock',   7500),
        (32, 'Funeral',                'Folk',         6800),
        (32, 'Moon Song',              'Acoustic',     7200),
        (32, 'Savior Complex',         'Indie Rock',   6500),
        (33, 'Nobody',                 'Alternative',  8500),
        (33, 'Washing Machine Heart',  'Indie Rock',   8200),
        (33, 'Your Best American Girl','Indie Rock',   9000),
        (33, 'Me and My Husband',      'Alternative',  7500),
        (34, 'Paprika',                'Alternative',  6800),
        (34, 'Be Sweet',               'Indie Rock',   6500),
        (34, 'Posing in Bondage',      'Alternative',  6000),
        (35, 'Coffee',                 'Pop',          5800),
        (35, 'Death Bed',              'Pop',          5500),
        (35, 'Care',                   'Indie Rock',   5000),
        (35, 'Talk',                   'Indie Rock',   4800),
        (36, 'This Is Home',           'Indie Rock',   4800),
        (36, 'Devil Town',             'Acoustic',     4500),
        (36, 'Lemon Boy',              'Indie Rock',   4200),
        (36, 'Green',                  'Acoustic',     3800),
        (37, 'Chaise Longue',          'Indie Rock',   3800),
        (37, 'Wet Dream',              'Alternative',  3500),
        (37, 'Oh No',                  'Indie Rock',   3200),
        (38, 'Lauren',                 'Electronic',   3300),
        (38, 'Show Me How',            'Electronic',   3100),
        (38, 'Numb',                   'Indie Rock',   2900),
        (39, 'Evergreen',              'R&B',          5200),
        (39, 'Kamikaze',               'Alternative',  4800),
        (39, 'Hit Me Up',              'R&B',          4500),
        (40, 'Photo ID',               'Pop',          4000),
        (40, 'Woo!',                   'Funk',         3800),
        (40, 'Grumpy Old Man',         'Pop',          3500),
        (41, 'Full Control',           'Indie Rock',   4800),
        (41, 'Pristine',               'Alternative',  4500),
        (41, 'Valentine',              'Alternative',  4000),
        (42, 'Circle the Drain',       'Alternative',  4600),
        (42, 'Night Swimming',         'Indie Rock',   4000),
        (42, 'Royal Screw Up',         'Alternative',  3800),
        (43, 'Not',                    'Folk',         5800),
        (43, 'Cattails',               'Indie Rock',   5500),
        (43, 'Simulation Swarm',       'Alternative',  5000),
        (44, 'Anchor',                 'Folk',         7800),
        (44, 'Fade',                   'Acoustic',     7500),
        (44, 'State Lines',            'Folk',         7000),
        (45, 'Coastline',              'Folk',         6800),
        (45, 'The Woods',              'Acoustic',     6500),
        (45, 'Voices',                 'Folk',         6200),
        (46, 'Pretty Girl',            'Lo-Fi',        9200),
        (46, 'Sofia',                  'Indie Rock',   9000),
        (46, 'Amoeba',                 'Lo-Fi',        8800),
        (46, 'Bags',                   'R&B',          8500),
        (47, 'We Fell in Love in October','Indie Rock',8800),
        (47, 'i wanna be your girlfriend','Alternative',8500),
        (47, 'Serotonin',              'Alternative',  8000),
        (48, 'Loving Is Easy',         'Indie Rock',   9000),
        (48, 'Best Friend',            'Pop',          8800),
        (48, 'Pluto Projector',        'Alternative',  8200),
        (49, 'ILYSB',                  'Pop',          8300),
        (49, 'Super Far',              'Pop',          8000),
        (49, 'Pink Skies',             'Indie Rock',   7800),
        (49, 'Good Girls',             'Pop',          7500),
        (50, 'Apocalypse',             'Ambient',      7800),
        (50, "Nothing's Gonna Hurt You Baby",'Ambient',7500),
        (50, 'Sunsetz',                'Indie Rock',   7200),
        (50, 'Sweet',                  'Indie Rock',   6800),
    ]
    cursor.executemany('INSERT INTO Track (ArtistID, Title, Genre, PlayCount) VALUES (?, ?, ?, ?)', tracks)

    conn.commit()
    conn.close()
    print(f"Database created with {len(artists)} artists and {len(tracks)} tracks!")

if __name__ == '__main__':
    create_database()