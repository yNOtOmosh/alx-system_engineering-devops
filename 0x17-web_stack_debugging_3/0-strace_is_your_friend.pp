# Puppet to fix the bug in wp-settings.php

exec { 'fix extension problem':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/localhost/bin/:/bin/'
}
