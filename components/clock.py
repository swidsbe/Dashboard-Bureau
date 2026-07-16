def clock_card_html():
    """Retourne le HTML de la carte Horloge : heure et date mises à
    jour côté navigateur toutes les secondes (sans rechargement)."""
    return """
    <div class="db-card db-clock-card">
        <div id="db-time" class="db-time">--:--:--</div>
        <div id="db-date" class="db-date">--</div>
        <div class="db-accent"></div>
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
    """
