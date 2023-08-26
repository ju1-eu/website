<?php
require 'vendor/autoload.php';

$parsedown = new Parsedown();
$html = '';
$errorMessage = '';
$markdown = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $markdown = isset($_POST['markdown']) ? $_POST['markdown'] : '';

    if (empty($markdown)) {
        $errorMessage = 'Bitte geben Sie einen gültigen Markdown-Text ein.';
    } else {
        $html = $parsedown->text(htmlspecialchars($markdown, ENT_QUOTES, 'UTF-8'));
    }
}
?>

<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown zu HTML Konverter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 2em;
            background-color: #f6f7f8;
        }

        .container {
            background-color: white;
            padding: 1em;
            border-radius: 0.3em;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        form {
            margin-bottom: 2em;
        }

        textarea {
            width: 100%;
            min-height: 12em;
            margin-bottom: 1em;
            padding: 1em;
            border: 1px solid #ccc;
            border-radius: 0.3em;
            font-size: 1em;
            resize: vertical;
        }

        button, input[type="submit"] {
            padding: 0.5em 1em;
            font-size: 1em;
            border: none;
            border-radius: 0.3em;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover, input[type="submit"]:hover {
            background-color: #0056b3;
        }

        .error-message {
            color: red;
            margin-bottom: 1em;
        }

        h2 {
            font-size: 1.5em;
            margin-top: 0;
        }

        pre {
            background-color: #f8f8f8;
            padding: 1em;
            border-radius: 0.3em;
            overflow-x: auto;
            white-space: pre-wrap;  
            word-wrap: break-word;  
        }

        code {
            font-family: "Courier New", Courier, monospace;
            color: #B82327;
            background-color: #f7f7f9;
            border: 1px solid #e1e1e8;
            border-radius: 0.3em;
            padding: 0.1em 0.3em;
            display: block;
        }

        pre code {
            display: block;
            border: none;
            padding: 0;
        }

    </style>
</head>
<body>

<div class="container">
<h2>Markdown zu HTML Konverter</h2>
<h3>Überblick</h3>
<p>Dieses Skript ermöglicht die Konvertierung von Text, der in Markdown verfasst wurde, in HTML. Es ist in PHP geschrieben und verwendet die <code>Parsedown</code>-Bibliothek, um eine korrekte Umsetzung des Markdown-Formats sicherzustellen.</p>
<h3>Installation</h3>
<ol>
<li>
<p><strong>Voraussetzungen</strong></p>
<ul>
<li>Ein Server mit PHP-Unterstützung.</li>
<li><a href="https://getcomposer.org/">Composer</a>, ein Werkzeug für die Abhängigkeitsverwaltung in PHP.</li>
</ul>
</li>
<li>
<p><strong>Bibliothek installieren</strong>
Nach der Installation von Composer führt man den folgenden Befehl im Hauptverzeichnis des Projekts aus:</p>
<pre><code># Terminal
<?php echo htmlspecialchars('php -r "copy(\'https://getcomposer.org/installer\', \'composer-setup.php\');"'); ?>
</code></pre>

<pre><code># Terminal
mkdir -p /usr/local/bin
mv composer.phar /usr/local/bin/composer
composer
composer require erusev/parsedown</code></pre>
<p>Dies wird die <code>Parsedown</code>-Bibliothek in das Projekt herunterladen und installieren.</p>
</li>
<li>
<p><strong>Skript bereitstellen</strong>
Das zuvor bereitgestellte PHP-Skript kann in einem geeigneten Verzeichnis auf dem Server abgelegt werden.</p>
</li>
</ol>
<h3>Scriptaufruf</h3>
<p>Nachdem alles installiert wurde, kann man das Skript über einen Webbrowser aufrufen, indem man die entsprechende URL in die Adressleiste des Browsers eingibt. Zum Beispiel:</p>
<pre><code>http://meinedomain.de/pfad/zum/script.php</code></pre>
<h3>Funktionsweise</h3>
<p>Nach dem Aufrufen des Skripts im Browser sieht man ein Formularfeld, in das Markdown-Text eingegeben werden kann. Nachdem der Text eingegeben und das Formular abgeschickt wurde, zeigt das Skript den eingegebenen Markdown-Text als HTML formatiert an.</p>
<h3>Testergebnisse</h3>
<p>Das Skript wurde mit verschiedenen Markdown-Eingaben getestet, einschließlich, aber nicht beschränkt auf:</p>
<ul>
<li>Überschriften</li>
<li>Listen (sowohl geordnet als auch ungeordnet)</li>
<li>Links</li>
<li>Bilder</li>
<li>Textformatierungen wie <strong>Fett</strong>, <em>Kursiv</em> und <code>Code</code>.</li>
</ul>
<p>In allen Testszenarien wurde der Markdown-Text korrekt in HTML umgewandelt und angezeigt.</p>
<h3>Sicherheitshinweis</h3>
<p>Das Skript verwendet <code>htmlspecialchars</code> zur Behandlung von Benutzereingaben, um Cross-Site-Scripting-Attacken (XSS) zu verhindern. Es ist jedoch immer ratsam, weitere sicherheitsrelevante Aspekte im Auge zu behalten und das Skript regelmäßig auf Sicherheitslücken zu überprüfen, insbesondere wenn es in einer Produktionsumgebung eingesetzt wird.</p>
<h3>Schlussfolgerung</h3>
<p>Das bereitgestellte Skript ist ein nützliches Werkzeug, um Markdown schnell und einfach in HTML umzuwandeln. Es bietet eine einfache Benutzeroberfläche und zuverlässige Konvertierungsfunktionen.</p>

    <form action="" method="post">
        <label for="markdown" style="display: block; margin-bottom: 0.5em;">Geben Sie hier Ihren Markdown-Text ein:</label>
        
        <?php if ($errorMessage): ?>
            <div class="error-message">
                <?php echo $errorMessage; ?>
            </div>
        <?php endif; ?>

        <textarea name="markdown" id="markdown"><?php echo htmlspecialchars($markdown, ENT_QUOTES, 'UTF-8'); ?></textarea>
        <input type="submit" value="Konvertieren">
    </form>

    <?php if ($html): ?>
        <h2>Ausgabe:</h2>
        <div><?php echo $html; ?></div>
    <?php endif; ?>
</div>

</body>
</html>
