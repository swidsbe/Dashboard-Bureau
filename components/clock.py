import streamlit.components.v1 as components


def render_clock():
    """Affiche une carte Horloge plein écran, avec heure et date
    mises à jour en temps réel côté navigateur (pas de rechargement
    de la page)."""

    html = """
    <html>
    <head>
    <style>
        :root {
            --sage: #8A9A82;
            --anthracite: #2E2E2E;
            --offwhite: #F5F1EA;
            --wood: #A9784C;
        }

        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background-color: var(--offwhite);
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }

        .db-wrapper {
            width: 100vw;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .db-card {
            background-color: #FFFFFF;
            border-radius: 40px;
            border: 2px solid var(--sage);
            box-shadow: 0 8px 30px rgba(46, 46, 46, 0.08);
            width: 85%;
            max-width: 900px;
            padding: 60px 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .db-time {
            font-size: 9vw;
            font-weight: 700;
            color: var(--anthracite);
            letter-spacing: 2px;
        }

        .db-date {
            margin-top: 20px;
            font-size: 2.2vw;
            font-weight: 400;
            color: var(--anthracite);
            text-transform: capitalize;
        }

        .db-accent {
            width: 80px;
            height: 4px;
            background-color: var(--wood);
            border-radius: 2px;
            margin-top: 24px;
        }
    </style>
    </head>
    <body>
        <div class="db-wrapper">
            <div class="db-card">
                <div id="db-time" class="db-time">--:--:--</div>
                <div id="db-date" class="db-date">--</div>
                <div class="db-accent"></div>
            </div>
        </div>

        <script>
        function updateClock() {
            const now = new Date();
            const time = now.toLocaleTimeString('fr-FR', {
                hour: '2-digit', minute: '2-digit', second: '2-digit'
            });
            const days = ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'];
            const months = ['janvier','février','mars','avril','mai','juin',
                             'juillet','août','septembre','octobre','novembre','décembre'];
            const date = days[now.getDay()] + ' ' + now.getDate() + ' ' + months[now.getMonth()];

            document.getElementById('db-time').innerText = time;
            document.getElementById('db-date').innerText = date;
        }
        updateClock();
        setInterval(updateClock, 1000);
        </script>
    </body>
    </html>
    """

    components.html(html, height=1000, scrolling=False)
