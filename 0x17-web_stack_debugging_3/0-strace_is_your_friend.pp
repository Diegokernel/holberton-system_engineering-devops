# Replace a line inside a file
exec { 'fixing php':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => ['usr/bin', 'usr/sbin', '/bin']
}
