# kills a process named killmenow
exec { 'pkill killmenow':
  path   => '/usr/bin:/usr/sbin:/bin'
}
