# Replace the number of allow files to open

exec { 'replace':
  cwd     => '/etc/default/',
  command => 'sed -i -e s/15/2048/g nginx',
  path    => ['/bin','/usr/bin','/usr/sbin'],
  }->

  exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin','/bin'],
}
