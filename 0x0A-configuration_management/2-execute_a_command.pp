# kill the killme process

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
