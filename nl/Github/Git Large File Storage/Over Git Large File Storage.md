GitHub beperkt de grootte van toegestane bestanden in repositories. Om bestanden te volgen die deze limiet overschrijden, kun je Git Large File Storage gebruiken.

Afhankelijk van je GitHub-plan gelden er verschillende maximale groottebeperkingen voor Git LFS.

| Product                   | Maximale bestandsgrootte |
|---------------------------|--------------------------|
| GitHub Free               | 2 GB                     |
| GitHub Pro                | 2 GB                     |
| GitHub Team               | 4 GB                     |
| GitHub Enterprise Cloud   | 5 GB                     |

Als je de per bestandslimiet van 5 GB overschrijdt, wordt het bestand stilzwijgend afgewezen door Git LFS.

Je kunt ook Git LFS gebruiken met GitHub Desktop. Voor meer informatie over het klonen van Git LFS-repositories in GitHub Desktop, zie "[Een repository van GitHub naar GitHub Desktop klonen](/en/desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)."

Je kunt kiezen of Git LFS-objecten zijn opgenomen in [broncode-archieven](/en/repositories/working-with-files/using-files/downloading-source-code-archives), zoals ZIP-bestanden en tarballs, die GitHub maakt voor je repository. Voor meer informatie, zie "[Beheren van Git LFS-objecten in archieven van je repository](/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-git-lfs-objects-in-archives-of-your-repository)."

## Pointerbestandsindeling

Het pointerbestand van Git LFS ziet er als volgt uit:

```plaintext
version https://git-lfs.github.com/spec/v1
oid sha256:4cac19622fc3ada9c0fdeadb33f88f367b541f38b89102a3f1261ac81fd5bcb5
size 84977953
```

Het volgt de `versie` van Git LFS die je gebruikt, gevolgd door een unieke identificatie voor het bestand (`oid`). Het slaat ook de `grootte` van het uiteindelijke bestand op.

**Opmerkingen**:
- Git LFS kan niet worden gebruikt met GitHub Pages-sites.
- Git LFS kan niet worden gebruikt met sjabloonrepositories.

## Meer lezen

- "[Samenwerken met Git Large File Storage](Samenwerken%20met%20Git%20Large%20File%20Storage.md)"