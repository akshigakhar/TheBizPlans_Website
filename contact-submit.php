<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

function respond(int $status, bool $success, string $message): never
{
    http_response_code($status);
    echo json_encode(['success' => $success, 'message' => $message]);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    respond(405, false, 'Method not allowed.');
}

// Silently accept automated submissions that fill the hidden honeypot field.
if (trim((string) ($_POST['website'] ?? '')) !== '') {
    respond(200, true, 'Your message has been received.');
}

$name = trim((string) ($_POST['name'] ?? ''));
$phone = trim((string) ($_POST['phone'] ?? ''));
$email = trim((string) ($_POST['email'] ?? ''));
$message = trim((string) ($_POST['message'] ?? ''));

if ($name === '' || $phone === '' || $email === '' || $message === '') {
    respond(422, false, 'Please complete all required fields.');
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    respond(422, false, 'Please enter a valid email address.');
}

if (strlen($name) > 100 || strlen($phone) > 30 || strlen($email) > 254 || strlen($message) > 5000) {
    respond(422, false, 'One or more fields are too long.');
}

// Prevent header injection while retaining international names and phone formatting.
$name = str_replace(["\r", "\n"], ' ', $name);
$phone = str_replace(["\r", "\n"], ' ', $phone);
$safeEmail = str_replace(["\r", "\n"], '', $email);
$subject = 'New website enquiry from ' . $name;
$body = "A new contact enquiry was submitted through TheBizPlans.com.\n\n"
    . "Name: {$name}\n"
    . "Phone: {$phone}\n"
    . "Email: {$safeEmail}\n\n"
    . "Message:\n{$message}\n";
$headers = [
    'From: The Biz Plans Website <info@thebizplans.com>',
    'Reply-To: ' . $safeEmail,
    'Content-Type: text/plain; charset=UTF-8',
];

$sent = mail(
    'info@thebizplans.com, jagga_atul@yahoo.com',
    $subject,
    $body,
    implode("\r\n", $headers)
);

if (!$sent) {
    respond(500, false, 'We could not send your message. Please call us or try again shortly.');
}

respond(200, true, 'Your message has been received by the team.');
