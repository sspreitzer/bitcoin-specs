# bitcoin (core)
for Fedora / CentOS / Red Hat Enterprise Linux

## WARNING

**This software is linked to cryptographic routines that might be unsuitable for
bitcoin use. Read more in this [here](https://bugzilla.redhat.com/show_bug.cgi?id=1020292#c29). 
Until bitcoin is officially included in the Fedora Linux distribution you are
strongly advised to be cautious about using these pre-built packages.
And of course be strongly advised that you are using this software on your own risk
without any warranties or guaranties.**

## Fedora

```bash
sudo dnf copr enable sspreitz/fun
sudo dnf install -y bitcoin bitcoin-cli
```

## CentOS / Red Hat Enterprise Linux

```bash
curl 'https://copr.fedorainfracloud.org/coprs/sspreitz/fun/repo/epel-7/sspreitz-fun-epel-7.repo' > /etc/yum.repos.d/copr-sspreitz-fun.repo
yum install -y bitcoin bitcoin-cli
```

