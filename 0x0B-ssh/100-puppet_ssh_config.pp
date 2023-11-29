#!/usr/bin/env bash
# using Puppet to make changes to my configuration file

file { 'etc/ssh/ssh_config':
  ensure  => present,
  content => "
      # SSH client configuration
      Host *
      IdentifyFile ~/.ssh/school
      PasswordAuthentication no
    ",
}
