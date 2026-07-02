// SPDX-License-Identifier: MIT
(function () {
  "use strict";

  const container = document.getElementById("content-list");
  if (!container) return;

  function text(value) {
    return value == null ? "" : String(value);
  }

  function meta(label, value) {
    const row = document.createElement("div");
    row.textContent = `${label}: ${text(value)}`;
    return row;
  }

  function renderItem(item) {
    const card = document.createElement("article");
    card.className = "card";
    card.dataset.cid = text(item.cid);
    card.dataset.stableId = text(item.id);

    const badge = document.createElement("span");
    badge.className = "badge";
    badge.textContent = text(item.type || "content");
    card.appendChild(badge);

    const title = document.createElement("h2");
    title.textContent = text(item.title || item.id);
    card.appendChild(title);

    const summary = document.createElement("p");
    summary.textContent = text(item.summary);
    card.appendChild(summary);

    const block = document.createElement("div");
    block.className = "meta";
    block.appendChild(meta("stable id", item.id));
    block.appendChild(meta("route", item.route));
    block.appendChild(meta("cid", item.cid));
    if (item.reference) {
      block.appendChild(meta("reference", item.reference.stable_ref));
      block.appendChild(meta("reference policy", item.reference.policy));
    }
    if (item.source_ref) {
      block.appendChild(meta("source snapshot", item.source_ref.snapshot_cid));
      block.appendChild(meta("source route", item.source_ref.route));
    }
    card.appendChild(block);
    return card;
  }

  fetch("data/content.json", { cache: "no-store" })
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((data) => {
      const items = Array.isArray(data.items) ? data.items : [];
      container.replaceChildren(...items.map(renderItem));
    })
    .catch((error) => {
      const message = document.createElement("p");
      message.textContent = `Unable to load demo content: ${error.message}`;
      container.replaceChildren(message);
    });
})();
