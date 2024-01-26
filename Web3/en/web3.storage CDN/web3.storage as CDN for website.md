It is possible to use Web3.Storage as a CDN for your images. Web3.Storage is a service that allows you to store data on the decentralized web using protocols like IPFS and Filecoin.

When you upload a file to Web3.Storage, it gets distributed across the IPFS network, and it's accessible from anywhere on the web. You can use the CID (Content Identifier) returned by Web3.Storage to construct a URL and use it in your application to serve images.

However, it's important to note that while Web3.Storage is a great way to leverage decentralized storage, it might not be as fast as traditional CDN providers for a couple of reasons:

1. **Propagation delay:** When you first upload a file, it can take some time for the file to be distributed across the network.

2. **Retrieval speed:** The speed at which files are served can depend on how close the nearest copy of the file is in the network. In some cases, this might be slower than a traditional CDN, which uses edge locations to store copies of the files close to the end users.

If speed is a critical factor for your application, you might want to consider using a traditional CDN. However, if you want to leverage the benefits of decentralized storage, Web3.Storage is a great option.