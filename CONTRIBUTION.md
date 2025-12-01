
# 📝 **Project Contributions – Team Breakdown**

This document summarizes the work done by each team member in the Networking Project.
Each member contributed to a different core component to ensure protocol correctness, functionality, documentation, and a successful live demo.

---

## 👤 **Member 1 – Protocol & Socket Developer (Server Developer)**

**Main Responsibilities:**

* Implemented the **raw TCP socket server** using `socket()`, `bind()`, `listen()`, and `accept()`.
* Developed and documented the **HTTP request parsing logic** (method, path, headers).
* Implemented correct **HTTP responses** including status line and essential headers.
* Ensured behavior matches **basic RFC 7230 HTTP protocol rules**.
* Wrote clean, well-commented networking code in `server.py`.

**Files Contributed:**

* `server.py`


---

## 👤 **Member 2 – Client Developer & Extra Feature Implementation**

**Main Responsibilities:**

* Built the **HTTP client** using raw TCP sockets.
* Manually constructed and sent HTTP GET requests.
* Implemented printing & handling of server responses.
* Added an extra feature (choose one as implemented):

  * Serving HTML files
  * Logging incoming server requests
  * Supporting additional methods such as **HEAD**
* Wrote clean, readable, and documented code in `client.py`.

**Files Contributed:**

* `client.py`
* Extra feature modules (if any)

---

## 👤 **Member 3 – Build System & Documentation Lead**

**Main Responsibilities:**

* Created the **Makefile** with required targets:

  * `make`
  * `make server`
  * `make client`
  * `make clean`
* Authored a complete **README.md** including:

  * How to compile the project
  * How to run the server
  * How to run the client
  * Example commands for testing
  * Team member roles
* Ensured the entire project compiles correctly from a **clean checkout** (fresh clone).
* Helped maintain project structure and directory organization.

**Files Contributed:**

* `README.md`
* `Makefile`

---

##  **Member 4 – Tester, Debugger & Demo Manager**

**Main Responsibilities:**

* Conducted extensive **testing** using `curl`, `telnet`, and `nc` (netcat).
* Helped identify and fix bugs during server/client interactions.
* Created this **CONTRIBUTION.md** file documenting roles and tasks.
* Prepared the complete **15-minute live demo plan**, including:

  * Order of presentation
  * Who explains what
  * Demonstration flow (server → client → features → Q&A)
* Verified that the final project works reliably for the professor’s evaluation.

**Files Contributed:**

* `CONTRIBUTION.md`

---

#  **Summary Table**

| Member | Role                          | Main Contribution                                  |
| ------ | ----------------------------- | -------------------------------------------------- |
|*Fatima*  | Protocol & Socket Developer   | Raw TCP server, HTTP parsing, response handling    |
| *ARIFUL*  | Client + Features Developer   | HTTP client, additional functionality              |
| *ARAFAT*  | Build & Documentation Lead    | Makefile, README, project structure                |
| *ABDULLAH*  | Tester & Contribution Manager | Testing, debugging, demo planning, CONTRIBUTION.md |




