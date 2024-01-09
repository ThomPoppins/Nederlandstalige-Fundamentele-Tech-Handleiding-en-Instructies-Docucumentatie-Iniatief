
For authorization, w3up services utilize ucanto, a Remote Procedure Call (RPC) framework built around UCAN (User Controlled Authorization Networks). UCANs provide a powerful capability-based authorization system, allowing fine-grained sharing of permissions through delegation on top of public key cryptography.

UCANs replace bearer tokens in traditional APIs for authorization with w3up. As any actor can be represented by a cryptographic keypair, permissions can be delegated to them. Users can interact directly with w3up, eliminating the need for additional back-end infrastructure to secure API keys. This extends to end users using applications integrated with w3up through their own keypair-based identity.

## UCANs in w3up and w3up-client

The w3up client and CLI handle UCANs details for you, but some underlying terms and concepts may be relevant to the API. UCAN-based APIs revolve around capabilities, consisting of an ability and a resource. Together, they determine the client's actions and the objects in the system that can be acted upon.

### Space

When you upload data to w3up, it associates with a unique Space, acting as a "namespace" for the uploaded data. Each Space corresponds to a DID (Decentralized Identity Document), using the key DID method (did:key:publicKey) with a corresponding private signing key.

Spaces are registered with an email address, and the Space DID:key serves as the "resource" in capability, while the ability is an action like store/add or store/remove. Spaces can be thought of as an "account" with web3.storage.

### Agent

To perform actions like store/add on a Space using the client or CLI, an Agent is required. An Agent, like a Space, corresponds to a did:key, and its private key is generated locally. It is analogous to a login session and corresponds to a UCAN delegation where a registered Space delegates its capabilities to the Agent.

### Delegation to Other Actors

Just as Spaces can delegate permissions to Agents you own, you can also delegate permissions to other actors' Agents. A common application is delegating permission to upload to your Space to your users.

## Backend Example

```javascript
// Backend code snippet demonstrating UCAN delegation
// (Note: This is a simplified example)

import * as Client from '@web3-storage/w3up-client';

async function backend(did) {
  // Load client with a specific private key
  const principal = Signer.parse(process.env.KEY);
  const client = await Client.create({ principal });

  // Add proof that this agent has been delegated capabilities on the space
  const proof = await parseProof(process.env.PROOF);
  const space = await client.addSpace(proof);
  await client.setCurrentSpace(space.did());

  // Create a delegation for a specific DID
  const audience = DID.parse(did);
  const abilities = ['store/add', 'upload/add'];
  const expiration = Math.floor(Date.now() / 1000) + (60 * 60 * 24); // 24 hours from now
  const delegation = await client.createDelegation(audience, abilities, { expiration });

  // Serialize the delegation and send it to the client
  const archive = await delegation.archive();
  return archive.ok;
}

// Function to parse proof from a base64 encoded CAR file
async function parseProof(data) {
  // Implementation details...
}
```

## Frontend Example

```javascript
// Frontend code snippet demonstrating UCAN usage
// (Note: This is a simplified example)

import * as Client from '@web3-storage/w3up-client';

async function frontend() {
  // Create a new client
  const client = await Client.create();

  // Fetch the delegation from the backend
  const apiUrl = `/api/w3up-delegation/${client.agent().did()}`;
  const response = await fetch(apiUrl);
  const data = await response.arrayBuffer();

  // Deserialize the delegation
  const delegation = await Delegation.extract(new Uint8Array(data));
  if (!delegation.ok) {
    throw new Error('Failed to extract delegation', { cause: delegation.error });
  }

  // Add proof that this agent has been delegated capabilities on the space
  const space = await client.addSpace(delegation.ok);
  client.setCurrentSpace(space.did());

  // READY to go!
}
```

These examples showcase a simplified workflow of UCAN delegation in the backend and frontend, allowing secure and flexible authorization for w3up services. Explore further possibilities in the "Architecture Options" section.