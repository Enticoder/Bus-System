**BusSystem**

A minimal command-line bus management and booking system in Python. `main.py` implements a `Bus` class and a `BusSystem` controller to add buses, list them, and book passenger seats through a simple interactive menu.

**Author:** Suraj Gupta — learned and implemented this project from YouTube tutorials.

**Features:**
- Add buses with `route`, `seats`, and `price`.
- List buses with current booked counts.
- Book seats per passenger with overbooking protection.
- Single-file, no external dependencies (`main.py`).

**Requirements:**
- Python 3.x

**Run**
Open a terminal in the `BusSystem` folder and run:

```bash
python main.py
```

**What to do after running (walkthrough to see outputs):**
1. Choose `1. Add Bus` and enter values when prompted, e.g. `CityA-CityB`, `40`, `12.5`.
   - The program prints `Bus added!`.
2. Choose `2. Show Buses` to list buses. You will see numbered entries showing `Route`, `Seats`, `Booked`, and `Price`.
3. Choose `3. Book Seat`:
   - The program shows the bus list; enter the bus number (e.g. `1`) and a passenger name (e.g. `Alice`).
   - On success the program prints: `Seat booked for Alice! Ticket Price: 12.5` and the bus `Booked` count increases.
4. Choose `2. Show Buses` again to verify the `Booked` count increment and internal passenger list.

**Understanding the code:**
- `Bus` (in `main.py`) holds `route`, `seats`, `price`, `booked` count and `passengers` list and provides `show_info()` and `book_seat()`.
- `BusSystem` manages a list of `Bus` objects and provides `add_bus()`, `show_buses()`, and `book_bus_seat()`.
- The `main()` loop handles the simple interactive CLI menu.

See the source: [main.py](main.py)

**Next improvements (optional):**
- Persist buses and bookings to a file or DB.
- Add input validation and error handling.
- Add seat cancellation and detailed seat selection.
- Add unit tests and a nicer CLI (e.g., `argparse`) or a web frontend.

