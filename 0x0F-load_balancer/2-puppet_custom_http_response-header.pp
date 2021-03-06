# Install nginx and set custom header response http
exec { 'update-pkg':
  command => '/usr/bin/apt-get update',
}
->package { 'nginx':
   ensure  => 'present',
}
->file_line { 'the header':
   ensure => present,
   path   => '/etc/nginx/sites-available/default',
   line   => "	location / {
   	   add_header X-Served-By ${hostname};",
   match  => '^\tlocation / {',
}
->service { 'nginx':
   ensure  => running,
   require => Package['nginx'],
}
->exec { 'nginx restart':
   command => '/usr/sbin/service nginx restart',
}
