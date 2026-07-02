![V-SeMo Logo](v-semo_repo_card.png)
[V-SeMo – Teaching General Relativity with virtual sector Models](https://v-semo.com/)

[V-SeMo](https://v-semo.com/) is a canvas tool based on fabric.js with the purpose to teach
General Relativity with virtual sector models.

## Quickstart

Clone the repository:
```
git clone https://github.com/SvenWeissenborn/V-SeMo-Public.git
```

V-SeMo needs to be delivered by a webserver. For local testing, the simple http server
provided by Python 3 works well — run it from inside the cloned folder:
```
python3 -m http.server 8080
```

Then open your browser at:
```
http://localhost:8080/sp_map.html?showExerciseBox=1&buildStartMarks=1
```

This loads a sphere-based sector model with a guided exercise box.

There are many other `*.html` files in the repo root to explore — each one references a
different sector model geometry and (optionally) a different guided exercise.

## Documentation

Further documentation — how the various `*.html` files are wired together, how to create a
new sector model, how to write a new guided exercise, and a full reference of the available
URL parameters — lives in the [Wiki](https://github.com/SvenWeissenborn/V-SeMo-Public/wiki):

- [Quickstart](https://github.com/SvenWeissenborn/V-SeMo-Public/wiki/Quickstart)
- [Parameter-Files](https://github.com/SvenWeissenborn/V-SeMo-Public/wiki/Parameter-Files)
- [Geometrie-Module](https://github.com/SvenWeissenborn/V-SeMo-Public/wiki/Geometrie-Module)
- [Exercise-Boxen](https://github.com/SvenWeissenborn/V-SeMo-Public/wiki/Exercise-Boxen)
- [URL-Parameter](https://github.com/SvenWeissenborn/V-SeMo-Public/wiki/URL-Parameter)

## V-SeMo in Action
![V-Semo used on a tablet device](documentation/images/tablet_line.png)
