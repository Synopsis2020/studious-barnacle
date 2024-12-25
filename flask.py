<?php
// Получаем значение из GET-запроса
if (isset($_GET['value'])) {
    $value = htmlspecialchars($_GET['value']); // Защита от XSS

    // Сохраняем значение в файл
    $data = ['value' => $value];
    file_put_contents('data.json', json_encode($data));
}
?>
