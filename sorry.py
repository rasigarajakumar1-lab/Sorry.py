from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="de">

<head>

<meta charset="UTF-8">
<meta name="viewpoirt" content="width=device-width, intial-scale=1.0">

<title>Für Matthukutty <3</title>

<style>

* {
box-sizing: border-box;
margin: 0;
padding: 0;
}

 body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                         Roboto, Helvetica, Arial, sans-serif;

            min-height: 100vh;

            background:
                radial-gradient(circle at 20% 20%, #ffd6e7 0%, transparent 35%),
                radial-gradient(circle at 80% 80%, #e7d5ff 0%, transparent 35%),
                linear-gradient(135deg, #fff0f6, #ffe5ef, #f5e9ff);

            color: #4a2635;

            overflow-x: hidden;
        }


        /* -------------------------
           SCHWEBENDE HERZEN
        ------------------------- */

        .heart {
            position: fixed;

            bottom: -50px;

            font-size: 25px;

            opacity: 0.55;

            pointer-events: none;

            animation: floatHeart linear infinite;

            z-index: 0;
        }

        .heart:nth-child(1) {
            left: 5%;
            animation-duration: 8s;
        }

        .heart:nth-child(2) {
            left: 18%;
            animation-duration: 11s;
            animation-delay: 2s;
        }

        .heart:nth-child(3) {
            left: 35%;
            animation-duration: 9s;
            animation-delay: 4s;
        }

        .heart:nth-child(4) {
            left: 55%;
            animation-duration: 12s;
            animation-delay: 1s;
        }

        .heart:nth-child(5) {
            left: 72%;
            animation-duration: 10s;
            animation-delay: 3s;
        }

        .heart:nth-child(6) {
            left: 90%;
            animation-duration: 8s;
            animation-delay: 5s;
        }


        @keyframes floatHeart {

            0% {
                transform:
                    translateY(0)
                    rotate(0deg);

                opacity: 0;
            }

            15% {
                opacity: 0.6;
            }

            100% {
                transform:
                    translateY(-110vh)
                    rotate(360deg);

                opacity: 0;
            }
        }


        /* -------------------------
           HAUPTCONTAINER
        ------------------------- */

        .container {

            position: relative;

            z-index: 2;

            width: 100%;

            min-height: 100vh;

            display: flex;

            justify-content: center;

            align-items: center;

            padding: 30px;
        }


        .card {

            width: min(92vw, 700px);

            padding: 50px 40px;

            background: rgba(255, 255, 255, 0.82);

            backdrop-filter: blur(15px);

            -webkit-backdrop-filter: blur(15px);

            border: 1px solid rgba(255,255,255,0.7);

            border-radius: 35px;

            box-shadow:
                0 30px 80px rgba(130, 60, 100, 0.18);

            text-align: center;

            animation: cardAppear 1s ease;

        }


        @keyframes cardAppear {

            from {
                opacity: 0;

                transform:
                    translateY(30px)
                    scale(0.96);
            }

            to {
                opacity: 1;

                transform:
                    translateY(0)
                    scale(1);
            }
        }


        /* -------------------------
           TEXT
        ------------------------- */

        .small-title {

            font-size: 13px;

            letter-spacing: 3px;

            text-transform: uppercase;

            color: #d75b87;

            font-weight: 700;

            margin-bottom: 15px;
        }


        h1 {

            font-size: clamp(38px, 8vw, 64px);

            line-height: 1.05;

            color: #a93664;

            margin-bottom: 20px;
        }


        h2 {

            font-size: 30px;

            color: #a93664;

            margin-bottom: 20px;
        }


        p {

            font-size: 18px;

            line-height: 1.75;

            margin: 15px 0;

            color: #65404e;
        }


        .big-heart {

            font-size: 70px;

            display: block;

            margin-bottom: 15px;

            animation: heartbeat 1.6s infinite;
        }


        @keyframes heartbeat {

            0%, 100% {
                transform: scale(1);
            }

            50% {
                transform: scale(1.12);
            }
        }


        .highlight {

            color: #d64f7e;

            font-weight: 700;
        }


        /* -------------------------
           BUTTONS
        ------------------------- */

        .button-area {

            margin-top: 30px;

            display: flex;

            justify-content: center;

            gap: 15px;

            flex-wrap: wrap;
        }


        button {

            border: none;

            padding: 15px 27px;

            border-radius: 999px;

            font-size: 16px;

            font-weight: 700;

            cursor: pointer;

            transition:
                transform 0.2s,
                box-shadow 0.2s;

            font-family: inherit;
        }


        .primary {

            background:
                linear-gradient(
                    135deg,
                    #e85b8a,
                    #c94473
                );

            color: white;

            box-shadow:
                0 10px 25px rgba(200, 60, 110, 0.3);
        }


        .primary:hover {

            transform: translateY(-3px) scale(1.03);

            box-shadow:
                0 15px 30px rgba(200, 60, 110, 0.4);
        }


        .secondary {

            background: #fff;

            color: #b43e6b;

            border: 2px solid #f0c2d3;
        }


        .secondary:hover {

            transform: scale(1.04);
        }


        /* -------------------------
           SEITEN
        ------------------------- */

        .page {

            display: none;

            animation: pageAppear 0.6s ease;
        }


        .page.active {

            display: block;
        }


        @keyframes pageAppear {

            from {

                opacity: 0;

                transform: translateX(25px);
            }

            to {

                opacity: 1;

                transform: translateX(0);
            }
        }


        /* -------------------------
           BRIEF
        ------------------------- */

        .letter {

            text-align: left;

            background: #fff8fb;

            border-radius: 20px;

            padding: 30px;

            margin-top: 25px;

            border: 1px solid #f6d7e3;

            box-shadow:
                inset 0 0 30px rgba(220, 100, 140, 0.05);
        }


        .letter p {

            font-size: 17px;
        }


        .signature {

            margin-top: 25px;

            text-align: right;

            font-style: italic;

            color: #b0446d;
        }


        /* -------------------------
           GRÜNDE
        ------------------------- */

        .reasons {

            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 15px;

            margin-top: 30px;
        }


        .reason {

            background: #fff7fa;

            border-radius: 20px;

            padding: 22px 15px;

            border: 1px solid #f6d5e2;

            transition: transform 0.2s;
        }


        .reason:hover {

            transform: translateY(-5px);
        }


        .reason .emoji {

            font-size: 35px;

            margin-bottom: 10px;
        }


        .reason strong {

            color: #a83d66;
        }


        /* -------------------------
           ABSCHLUSS
        ------------------------- */

        .final {

            display: none;
        }


        .final.show {

            display: block;

            animation: finalAppear 1s ease;
        }


        @keyframes finalAppear {

            from {

                opacity: 0;

                transform: scale(0.8);
            }

            to {

                opacity: 1;

                transform: scale(1);
            }
        }


        .big-message {

            font-size: clamp(35px, 8vw, 60px);

            font-weight: 800;

            color: #d33e72;

            margin: 25px 0;
        }


        .confetti {

            position: fixed;

            top: -20px;

            font-size: 25px;

            pointer-events: none;

            z-index: 20;

            animation: confettiFall 3s linear forwards;
        }


        @keyframes confettiFall {

            to {

                transform:
                    translateY(110vh)
                    rotate(720deg);

                opacity: 0;
            }
        }


        /* -------------------------
           NEIN BUTTON
        ------------------------- */

        #noButton {

            background: #f4eef1;

            color: #8b6876;

            position: relative;
        }


        /* -------------------------
           MOBILE
        ------------------------- */

        @media (max-width: 600px) {

            .container {

                padding: 15px;
            }

            .card {

                padding: 35px 22px;

                border-radius: 27px;
            }

            p {

                font-size: 16px;
            }

            .reasons {

                grid-template-columns: 1fr;
            }

            .letter {

                padding: 22px;
            }
        }

    </style>

</head>


<body>


    <!-- HERZEN -->

    <div class="heart">❤️</div>
    <div class="heart">💗</div>
    <div class="heart">💕</div>
    <div class="heart">💖</div>
    <div class="heart">❤️</div>
    <div class="heart">💞</div>


    <div class="container">

        <div class="card">


            <!-- SEITE 1 -->

            <section id="page1" class="page active">

                <span class="big-heart">🥺</span>

                <div class="small-title">
                    Eine offizielle Mitteilung
                </div>

                <h1>
                    Für Matthukutty ❤️
                </h1>

                <p>
                    Ich muss dir etwas sagen...
                </p>

                <p>
                    Und ich dachte mir,
                    eine normale Nachricht wäre
                    dafür irgendwie zu langweilig.
                </p>

                <div class="button-area">

                    <button
                        class="primary"
                        onclick="nextPage(2)">

                        Okay... erzähl. ❤️

                    </button>

                </div>

            </section>



            <!-- SEITE 2 -->

            <section id="page2" class="page">

                <span class="big-heart">😭</span>

                <div class="small-title">
                    Die Wahrheit
                </div>

                <h2>
                    Okay... ich gebe es zu.
                </h2>

                <p>
                    Ich war heute
                    <span class="highlight">
                        gemein zu dir.
                    </span>
                </p>

                <p>
                    Und ja...
                    das war nicht besonders nett von mir.
                </p>

                <p>
                    Deshalb möchte ich dir
                    ganz ehrlich sagen:
                </p>

                <h2>
                    Es tut mir leid. ❤️
                </h2>

                <div class="button-area">

                    <button
                        class="primary"
                        onclick="nextPage(3)">

                        Weiter lesen 💌

                    </button>

                </div>

            </section>



            <!-- SEITE 3 -->

            <section id="page3" class="page">

                <div class="small-title">
                    Eine kleine Erklärung
                </div>

                <h2>
                    Ein Brief für dich 💌
                </h2>


                <div class="letter">

                    <p>
                        Lieber Matthukutty,
                    </p>

                    <p>
                        manchmal bin ich einfach ein bisschen
                        schwierig.
                        Und heute war definitiv einer dieser Tage.
                    </p>

                    <p>
                        Ich wollte dich nicht verletzen
                        oder dir ein schlechtes Gefühl geben.
                    </p>

                    <p>
                        Auch wenn ich heute vielleicht
                        nicht besonders nett war,
                        ändert das nichts daran,
                        wie wichtig du mir bist.
                    </p>

                    <p>
                        Deshalb:
                        <strong>
                            Es tut mir wirklich leid.
                        </strong>
                    </p>

                    <p>
                        Und jetzt hör bitte auf,
                        sauer auf mich zu sein. 😭
                    </p>

                    <div class="signature">
                        Deine chellummm ❤️
                    </div>

                </div>


                <div class="button-area">

                    <button
                        class="primary"
                        onclick="nextPage(4)">

                        Noch eine Sache... 🥺

                    </button>

                </div>

            </section>



            <!-- SEITE 4 -->

            <section id="page4" class="page">

                <div class="small-title">
                    Warum du mir wichtig bist
                </div>

                <h2>
                    Nur damit das klar ist:
                </h2>

                <div class="reasons">

                    <div class="reason">

                        <div class="emoji">
                            ❤️
                        </div>

                        <strong>
                            Du bist mir wichtig
                        </strong>

                        <p>
                            Mehr als ich manchmal
                            zeigen kann.
                        </p>

                    </div>


                    <div class="reason">

                        <div class="emoji">
                            🥹
                        </div>

                        <strong>
                            Ich liebe dich
                        </strong>

                        <p>
                            Auch wenn ich manchmal
                            komplett gemein und kalt bin.
                        </p>

                    </div>


                    <div class="reason">

                        <div class="emoji">
                            🫶
                        </div>

                        <strong>
                            Bitte bleib bei mir
                        </strong>

                        <p>
                            Ich werde versuchen,
                            weniger gemein zu sein. ❤️
                        </p>

                    </div>

                </div>


                <div class="button-area">

                    <button
                        class="primary"
                        onclick="nextPage(5)">

                        Letzte Frage... 👀

                    </button>

                </div>

            </section>



            <!-- SEITE 5 -->

            <section id="page5" class="page">

                <span class="big-heart">
                    🥺
                </span>

                <div class="small-title">
                    Die wichtigste Frage
                </div>

                <h2>
                    Nimmst du meine Entschuldigung an?
                </h2>

                <div class="button-area">

                    <button
                        class="primary"
                        onclick="acceptApology()">

                        Ja ❤️

                    </button>


                    <button
                        id="noButton"
                        onclick="moveNoButton()">

                        Nein 😤

                    </button>

                </div>

            </section>



            <!-- FINALE -->

            <section id="final" class="final">

                <span class="big-heart">
                    😭❤️
                </span>

                <div class="small-title">
                    Offiziell bestätigt
                </div>

                <div class="big-message">
                    JAAAAA ❤️
                </div>

                <p>
                    Die Entschuldigung wurde angenommen.
                </p>

                <p>
                    Du bist jetzt offiziell wieder
                    <span class="highlight">
                        mein Matthukutty.
                    </span>
                </p>

                <p>
                    Ich liebe dichhhhh. ❤️
                </p>

                <div class="button-area">

                    <button
                        class="primary"
                        onclick="celebrate()">

                        Noch mehr Liebe ❤️

                    </button>

                </div>

            </section>


        </div>

    </div>



    <script>


        /* -------------------------
           SEITEN WECHSELN
        ------------------------- */

        function nextPage(number) {

            document
                .querySelectorAll(".page")
                .forEach(function(page) {

                    page.classList.remove("active");

                });


            document
                .getElementById("page" + number)
                .classList.add("active");
        }



        /* -------------------------
           ENTSCHULDIGUNG ANNEHMEN
        ------------------------- */

        function acceptApology() {

            document
                .querySelectorAll(".page")
                .forEach(function(page) {

                    page.style.display = "none";

                });


            document
                .getElementById("final")
                .classList.add("show");


            celebrate();
        }



        /* -------------------------
           NEIN BUTTON
        ------------------------- */

        function moveNoButton() {

            const button =
                document.getElementById("noButton");


            const maxX =
                window.innerWidth -
                button.offsetWidth -
    20;


const maxY =
    window.innerHeight -
    button.offsetHeight -
    20;


const x =
    Math.random() * maxX;


const y =
    Math.random() * maxY;


button.style.position = "fixed";

button.style.left = x + "px";

button.style.top = y + "px";
}

/* -------------------------
   KONFETTI
------------------------- */

function celebrate() {

    const emojis = [
        "❤️",
        "💗",
        "💕",
        "💖",
        "✨",
        "🥹",
        "🫶"
    ];


    for (let i = 0; i < 35; i++) {

        const item =
            document.createElement("div");


        item.className = "confetti";


        item.innerText =
            emojis[
                Math.floor(
                    Math.random() *
                    emojis.length
                )
            ];


        item.style.left =
            Math.random() * 100 + "vw";


        item.style.animationDuration =
            (2 + Math.random() * 2) + "s";


        item.style.animationDelay =
            Math.random() * 0.8 + "s";


        document
            .body
            .appendChild(item);


        setTimeout(function() {

            item.remove();

        }, 4000);
    }
}


</script>


</body>

</html>
"""


@app.route("/")
def home():

    return render_template_string(HTML)


if __name__ == "__main__":

    app.run(debug=True)



                
