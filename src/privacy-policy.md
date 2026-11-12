# ODIN privacy policy

> **Draft — needs the owner's review before publishing; not legal advice.**
> Items marked **UNSURE** could not be confirmed from the code and need a decision or a check.

Last updated: UNSURE (set the date when the owner publishes this).

## The short version

- **Outland Dynamics runs no servers for ODIN and collects nothing about you.** We have no
  accounts, no analytics, no advertising, no tracking and no crash-reporting service.
- The ODIN app talks to **one place: the ODIN server you (or the person who invited you) run**,
  for example on a home NAS. Everything ODIN knows about you is stored on that server or on your
  phone, not with us.
- That server may look up public information about your **titles** (show and movie names, book
  titles and authors) from a few public catalogues, so it can show posters, summaries and cast.
  It never sends your name, email, files, folder paths or viewing history. The server owner can
  turn this off.

## Who we are

ODIN is made by Outland Dynamics. You buy the app once through Apple's App Store or Google Play;
the payment is handled by Apple or Google under their own privacy policies. We do not receive
your card details.

Contact: UNSURE (the owner to add a support email address or web page).

## What the app does with your data

The app connects only to the server address you type in, scan, or open from an invitation link.
It keeps on your phone:

- the server address, and your sign-in for that server (a session key, stored in the phone's
  secure storage: iOS Keychain or Android Keystore);
- your app settings and some personal lists kept only on the phone, for example book notes and
  bookmarks, your watchlist, recent searches, reading goal and layout choices.

Android backups of the app are turned off (`allowBackup: false`), so this data stays on the
phone. **UNSURE:** on iPhone, app data may be included in your own iCloud or computer backup, as
for most apps; we have not turned that off. Either way it goes to your own backup, not to us.

The app has no analytics, advertising or crash-reporting code, and no third-party tracking SDKs.

The phone does not contact any other site to show you pictures. TV show artwork (from TVmaze),
movie posters and book covers are all fetched by your server and passed to the phone, so those
sites never see your phone's internet address. Your server keeps copies in its own data folder
(see below).

If you tap a link in the app (for example "TVmaze", a book's source page, the install guide or
this policy), it opens in your browser and that website's own privacy policy applies.

## What your ODIN server stores

The server belongs to its owner, not to us. It keeps its data in its own database and data
folder on the machine it runs on (typically two Docker volumes on a NAS), plus any backups the
owner makes. We cannot see or reach it.

It stores:

- **Accounts:** the owner, and each invited person's first name, email address and password
  (as a one-way scrypt hash, never the password itself).
- **Invitations:** the invited email address, which libraries were shared, and when the
  invitation was sent, accepted or cancelled. The invitation code is stored only as a hash.
- **Signed-in devices:** a device name, when it signed in and was last used (the session key is
  stored only as a hash).
- **Your activity, per person:** watch and listening progress, ratings, reading status (want to
  read, reading, read), TV playlists and comic reading orders.
- **Library information:** the owner's library names, folder locations, and the catalogue the
  server builds from the files (titles, years, episode lists, covers, posters and TV artwork it
  downloaded, and so on).
  Original media files are never changed.
- **Artwork from your own files:** for movies and shows without online artwork, the server
  reads poster images beside the media (such as `poster.jpg` or `folder.jpg`) and cover art
  stored inside video files, and keeps resized copies in its data folder. This is read on the
  server only; nothing about these files is sent anywhere.
- **Server logs:** each request's method, path (without its query) and the device's network
  address, written to the server's console log (for example `docker logs`). Sign-in keys are
  removed from logs. How long logs are kept depends on the owner's Docker settings.

Invited people see only the libraries shared with them. Other people can see an average rating
only once at least three people have rated an item, so one person's exact score is not revealed.

## How to delete your data

- **Delete your account yourself.** In the app: Home → **Account** → **Delete my account**,
  enter your password and confirm. This deletes, on that server, at once and for good: your
  sign-in (first name, email and password hash) and every device signed in with it, which
  libraries you can see, your watch and listening progress, ratings, reading status, TV playlists,
  the comic reading orders you made (people who follow them lose them too), any password reset
  codes, and the invitations sent to your email address. The media and other people's data are
  not touched. Nothing identifying you is kept.
- **Or ask the server owner**, who can remove you in Sharing (**Remove from server**). That
  deletes exactly the same data.
- **On your phone:** notes, bookmarks, your watchlist and other lists kept only on the phone
  are deleted when you delete the app.
- The **server owner** cannot delete their own account in the app; to remove ODIN and all its
  data, they follow the install guide's Uninstall section.
- **UNSURE:** copies in backups the owner already made, and lines in the server's console log,
  are not removed by deleting an account; they go when the owner deletes or replaces those
  backups and logs.

## Who the server contacts

All of these are contacted by **the server**, not by Outland Dynamics, and only for information
about titles. No personal data is sent: no names, emails, file names, folder paths, viewing
history or device information. Requests are spaced out and use fixed addresses.

| Service | What it is for | What is sent | On by default? |
| --- | --- | --- | --- |
| [TVmaze](https://www.tvmaze.com) (`api.tvmaze.com`, artwork from `static.tvmaze.com`) | TV show details, episodes, cast, artwork | The show title (as read from the folder name); for artwork, the image's address from TVmaze's own data | Yes, for TV libraries. `UMP_METADATA=off` turns it off |
| [OMDb](https://www.omdbapi.com) (`www.omdbapi.com`, `img.omdbapi.com`) | Movie details, posters, ratings; TV series posters, episode ratings and episode titles TVmaze lacks | A title and year, or an IMDb id, plus the owner's own OMDb key (or Poster API key) | **No.** Only if the owner adds their own `UMP_OMDB_API_KEY`. `UMP_METADATA=off` also turns it off |
| [Metron](https://metron.cloud) (`metron.cloud`) | Comic writer and artist credits for comics without ComicInfo.xml | A comic series name and year, Metron's own ids and issue numbers, with the owner's own Metron account (API token, or username and password) | **No.** Only if the owner adds their own `UMP_METRON_TOKEN` (or username and password). `UMP_METADATA=off` also turns it off |
| [Open Library](https://openlibrary.org) (`openlibrary.org`, `covers.openlibrary.org`, `archive.org`) | Book details and covers | A book title and author | Yes, for book libraries. `UMP_METADATA=off` turns it off |
| [Google Books](https://books.google.com) (`www.googleapis.com`, `books.google.com`) | Book details and covers when Open Library has none | A book title and author | Yes, as above |
| Audible's public catalogue (`api.audible.com`, covers from `m.media-amazon.com`) | Audiobook narrators, length, series, covers | A title and author | Yes, for audiobook libraries, as above |

Each service sees the server's internet address, as any website would, and applies its own
privacy policy. TVmaze's data is used under its CC BY-SA licence and credited in the app. So is
Metron's (CC BY-SA 4.0): a series page that shows Metron's names says "via Metron", with a link.

**UNSURE:** Audible publishes no terms for its catalogue search; the owner should confirm it is
acceptable to use before release.

**Email.** If the owner sets up email (`UMP_SMTP_*`), invitation emails are sent through the
**owner's own** mail account (for example their Gmail). The invitation contains the server
address and a one-time code. Without email set up, the owner sends the invitation by hand.

**Video transcoding.** If the owner wants transcoding, they download Cisco's OpenH264 library
themselves and copy it to the server. The server does not download it or contact Cisco.

The server does not contact Outland Dynamics for licences, updates or anything else.

## Reporting a problem

"Report a problem" (in About ODIN) opens **your own email app** with a message you can read and
edit before sending. It includes the app and server versions and your phone's operating system.
For the server owner it also includes a diagnostics summary (disk space, backups, scans) without
passwords, keys or email addresses. Nothing is sent unless you send that email yourself.

## Children

ODIN is not directed at children under 13, and Outland Dynamics does not knowingly collect data
from anyone, including children. Whether a child uses ODIN, and what media they can see, is up
to the server owner and the child's parent or guardian.

## Changes to this policy

If this policy changes, the new version will be published at the same address with a new date.
The history of changes is kept in the project's repository.

## Contact

Questions about this policy: UNSURE (contact address to be added by the owner). Questions about
your data on a particular ODIN server go to that server's owner.
