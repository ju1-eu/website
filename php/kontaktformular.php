<?php
// Hier könnten Sie die Daten aus dem Kontaktformular verarbeiten (z.B. in eine Datenbank einfügen oder per E-Mail senden)

// Daten aus POST holen
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// Hier könnten Sie einen E-Mail-Versand oder eine Datenbankeinfügung einfügen

// Nach der Verarbeitung zur Startseite weiterleiten
header('Location: ../index.html');
exit;
?>
