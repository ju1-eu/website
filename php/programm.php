<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Durch 7 teilbare Zahlen</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }

        form {
            margin-bottom: 20px;
        }

        .error {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
<h2>Was macht das Programm?</h2>
<p>Das Programm ermöglicht es dem Benutzer, zwei Grenzwerte einzugeben. Nach dem Absenden des Formulars berechnet das Programm alle durch 7 teilbaren Zahlen zwischen diesen beiden Grenzen und gibt sie aus. Bei ungültigen oder nicht numerischen Eingaben zeigt das Programm eine Fehlermeldung an und fordert den Benutzer auf, gültige Zahlen einzugeben.</p>


<!-- Einfaches Formular zur Eingabe von Start- und Endwert -->
<form action="programm.php" method="post">
    <label for="start">Startwert:</label>
    <input type="text" id="start" name="start" required>
    <label for="end">Endwert:</label>
    <input type="text" id="end" name="end" required>
    <input type="submit" value="Berechnen">
</form>

<?php
// Überprüft, ob das Formular gesendet wurde
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $start = trim($_POST["start"]); // Entfernt überflüssige Leerzeichen
    $end = trim($_POST["end"]);

    // Überprüfung, ob die Eingaben numerisch sind
    if (!is_numeric($start) || !is_numeric($end)) {
        echo "<div class='error'>Bitte geben Sie gültige Zahlen ein.</div>";
    } else {
        $start = intval($start);
        $end = intval($end);

        echo "<h2>Durch 7 teilbare Zahlen zwischen $start und $end:</h2>";
        echo "<ul>";
    
        // Durchläuft die Zahlen zwischen Start und Ende und prüft, ob sie durch 7 teilbar sind
        for ($i = $start; $i <= $end; $i++) {
            if ($i % 7 == 0) {
                echo "<li>$i</li>";
            }
        }

        echo "</ul>";
    }
}
?>

</body>
</html>
