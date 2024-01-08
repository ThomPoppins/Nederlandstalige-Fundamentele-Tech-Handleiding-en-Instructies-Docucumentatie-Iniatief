
GitHub limits the size of files allowed in repositories. To track files beyond this limit, you can use Git Large File Storage.

Different maximum size limits for Git LFS apply depending on your GitHub plan.

| Product                   | Maximum file size |
|---------------------------|-------------------|
| GitHub Free               | 2 GB              |
| GitHub Pro                | 2 GB              |
| GitHub Team               | 4 GB              |
| GitHub Enterprise Cloud   | 5 GB              |

If you exceed the per file limit of 5 GB, the file will be rejected silently by Git LFS.

You can also use Git LFS with GitHub Desktop. For more information about cloning Git LFS repositories in GitHub Desktop, see "[Cloning a repository from GitHub to GitHub Desktop](/en/desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)."

You can choose whether Git LFS objects are included in [source code archives](/en/repositories/working-with-files/using-files/downloading-source-code-archives), such as ZIP files and tarballs, that GitHub creates for your repository. For more information, see "[Managing Git LFS objects in archives of your repository](/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-git-lfs-objects-in-archives-of-your-repository)."

## Pointer file format

Git LFS's pointer file looks like this:

```plaintext
version https://git-lfs.github.com/spec/v1
oid sha256:4cac19622fc3ada9c0fdeadb33f88f367b541f38b89102a3f1261ac81fd5bcb5
size 84977953
```

It tracks the `version` of Git LFS you're using, followed by a unique identifier for the file (`oid`). It also stores the `size` of the final file.

**Notes**:
- Git LFS cannot be used with GitHub Pages sites.
- Git LFS cannot be used with template repositories.

## Further reading

- "[Collaboration with Git Large File Storage](Collaboration%20with%20Git%20Large%20File%20Storage.md)"
