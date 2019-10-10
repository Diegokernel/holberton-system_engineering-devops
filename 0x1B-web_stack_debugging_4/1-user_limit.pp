# fixes the limit of nginx server

exec {'fix-limit-nginx':
  command  => "sed -i 's/nofile 5/nofile 1000/g' /etc/security/limits.conf;\
              sed -i 's/nofile 4/nofile 1000/g' /etc/security/limits.conf",
  provider => 'shell';
}
