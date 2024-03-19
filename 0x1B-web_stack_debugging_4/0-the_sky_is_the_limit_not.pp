# increase amount of traffic on nginx server

exec { 'nginx-fix':
  path    => '/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx"
}
exec { 'nginx reboot':
  command => '/usr/sbin/service ngnx restart'
}
