# Crono: Simple cronometer script
Cronometer for linux, watch your to do time

## run it with: 
```shell
$ python3 crono.py
```
## Do not forget installing dependencies

I use this script this way:
> I've create a function into .zshrc

```zsh
function crono(){
  python3 /usr/bin/crono.py $1 $2
}
```
> After that just:
```shell
$ mv crono.py /usr/bin/crono.py
```
> Restart terminal and use it :)


#Thank you :D
