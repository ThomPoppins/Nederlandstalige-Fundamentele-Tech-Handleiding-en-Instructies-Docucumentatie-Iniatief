Natuurlijk, hier is de tekst geformatteerd in een gestructureerd Markdown-bestand in het Nederlands:

```markdown
# Samenwerken met Git Large File Storage

## In dit artikel

- [Grote bestanden bekijken in pull-aanvragen](#grote-bestanden-bekijken-in-pull-aanvragen)
- [Grote bestanden pushen naar forks](#grote-bestanden-pushen-naar-forks)
- [Meer lezen](#meer-lezen)

Met Git LFS ingeschakeld kun je grote bestanden ophalen, aanpassen en pushen, net zoals je zou verwachten bij elk bestand dat Git beheert. Echter, een gebruiker die geen Git LFS heeft geïnstalleerd, zal een andere workflow ervaren.

Als medewerkers van jouw repository geen Git LFS geïnstalleerd hebben, zullen ze geen toegang hebben tot het originele grote bestand. Als ze proberen jouw repository te klonen, zullen ze alleen de pointerbestanden ophalen en geen toegang hebben tot enige werkelijke data.

**Tip:** Om gebruikers zonder Git LFS te helpen, raden we aan richtlijnen voor repositorybijdragers in te stellen die beschrijven hoe ze met grote bestanden kunnen werken. Bijvoorbeeld, je kunt bijdragers vragen om grote bestanden niet te wijzigen, of om wijzigingen te uploaden naar een bestandsdelingsdienst zoals Dropbox of Google Drive. Voor meer informatie, zie ["Richtlijnen instellen voor repositorybijdragers."](#meer-lezen)

## Grote bestanden bekijken in pull-aanvragen

GitHub rendert sommige Git LFS-objecten niet in pull-aanvragen. Alleen het pointerbestand wordt getoond, met inhoud vergelijkbaar met het volgende:

```plaintext
+version https://git-lfs.github.com/spec/vi
+id sha256:7194bdd797bde471a6e29b4fa9c8c2278b3c4dadfc5cb2c36d7f4531dc6cb8f
+size 17330
```

Voor meer informatie over pointerbestanden, zie ["Over Git Large File Storage."](#over-git-large-file-storage)

Om wijzigingen in grote bestanden te bekijken, check de pull-aanvraag lokaal om de verschillen te bekijken. Voor meer informatie, zie ["Pull-aanvragen lokaal uitchecken."](#meer-lezen)

## Grote bestanden pushen naar forks

Het pushen van grote bestanden naar forks van een repository telt mee voor de bandbreedte- en opslaglimieten van de ouderrepository, in plaats van de limieten van de fork-eigenaar.

Je kunt Git LFS-objecten naar openbare forks pushen als het repositorynetwerk al Git LFS-objecten heeft of als je schrijftoegang hebt tot de hoofdmap van het repositorynetwerk.
```

Dit Markdown-bestand biedt een gestructureerde weergave van de inhoud met koppen, subkoppen en verwijzingen naar meer informatie. Pas dit gerust aan naar gelang van je voorkeuren of specifieke behoeften.