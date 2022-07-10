import tkinter
from tkinter import StringVar, messagebox
from time_tracker import TimeTracker
from datauploader import DataUploader
import json
import webbrowser


def load_userdata() -> dict:
    try:
        with open("userdata.json") as file:
            user_data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="No user data.",
                               message="No user data was found. Please login or create new user before using the time tracker!!!")
        user_data = {}
    return user_data


def update_time():
    time_passed = tracker.get_seconds()
    hours = time_passed//3600
    minutes = time_passed % 3600//60
    seconds = time_passed % 3600 % 60
    timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    if not tracker.is_running:
        uploader.upload_hours(tracker.get_hours())


def change_graph(event):
    global graph
    graph = user_data["graphs"][graph_list.curselection()[0]]

    uploader.change_graph(graph["id"])


def create_graph():
    graph_id = graph_id_entry.get()
    graph_name = graph_name_entry.get()
    graph_units = graph_units_entry.get()
    graph = uploader.create_new_graph(graph_id, graph_name, graph_units)
    graphs.append(graph['name'])
    user_data["graphs"].append(graph)
    update_graph_list()

    save_user_data()


def delete_graph():
    user_data["graphs"].remove(graph)
    graphs.remove(graph["name"])
    graph_list.select_set(0)

    update_graph_list()

    uploader.delete_graph()

    change_graph(None)

    save_user_data()


def login():
    username = username_entry.get()
    token = token_entry.get()
    uploader.login(username, token)

    global user_data
    user_data = {"username": username, "token": token, "graphs": []}


def create_user():
    global user_data
    username = username_entry.get()
    token = token_entry.get()
    user_data = uploader.create_new_user(username, token)
    save_user_data()


def update_graph_list():
    list_items = StringVar(value=graphs)
    graph_list.config(listvariable=list_items)


def save_user_data():
    with open("userdata.json", "w") as file:
        json.dump(user_data, file, indent=4)


def open_graph():
    webbrowser.open(graph["link"])


if __name__ == '__main__':
    user_data = load_userdata()
    if not user_data == {}:
        username = user_data["username"]
        token = user_data["token"]
        graph = user_data["graphs"][0]
        uploader = DataUploader(username, token, graph["id"])
        graphs = [x["name"] for x in user_data["graphs"]]
    else:
        uploader = DataUploader()
        graphs = []

    tracker = TimeTracker(update_time)

    window = tkinter.Tk()
    window.minsize(width=800, height=600)
    window.title("Time Tracker")
    window.columnconfigure(2, minsize=100)

    """The timer"""
    timer_label = tkinter.Label(text="00:00:00", font=("Ariel", 48))
    timer_label.grid(column=0, row=0, columnspan=2, sticky="EW")

    start_button = tkinter.Button(text="Start", command=tracker.start_tracker)
    start_button.grid(column=0, row=1, sticky="EW")
    stop_button = tkinter.Button(text="Stop", command=tracker.stop_tracker)
    stop_button.grid(column=1, row=1, sticky="EW")

    """Graph list and new graph creation"""
    graphs_label = tkinter.Label(text="Graphs:")
    graphs_label.grid(column=3, row=0, sticky="EW")

    list_items = StringVar(value=graphs)
    graph_list = tkinter.Listbox(
        height=10, listvariable=list_items, selectmode="browse")
    graph_list.bind('<<ListboxSelect>>', change_graph)
    graph_list.grid(column=4, row=0)

    graph_id_label = tkinter.Label(text="Graph ID:")
    graph_name_label = tkinter.Label(text="Graph Name:")
    graph_units_label = tkinter.Label(text="Units:")
    graph_id_entry = tkinter.Entry()
    graph_name_entry = tkinter.Entry()
    graph_units_entry = tkinter.Entry()
    create_graph_button = tkinter.Button(
        text="Create Graph", command=create_graph)

    delete_graph_button = tkinter.Button(
        text="Delete Selected Graph", command=delete_graph)
    delete_graph_button.grid(column=4, row=1, sticky="EW")

    graph_id_label.grid(column=3, row=2, sticky="EW")
    graph_name_label.grid(column=3, row=3, sticky="EW")
    graph_units_label.grid(column=3, row=4, sticky="EW")

    graph_id_entry.grid(column=4, row=2, sticky="EW")
    graph_name_entry.grid(column=4, row=3, sticky="EW")
    graph_units_entry.grid(column=4, row=4, sticky="EW")

    create_graph_button.grid(column=4, row=5, sticky="EW")

    """User login or creating new user"""
    username_label = tkinter.Label(text="Username:")
    username_entry = tkinter.Entry()
    username_label.grid(column=0, row=2, sticky="")
    username_entry.grid(column=1, row=2, sticky="EW")

    token_label = tkinter.Label(text="Token:")
    token_entry = tkinter.Entry()
    token_label.grid(column=0, row=3, sticky="EW")
    token_entry.grid(column=1, row=3, sticky="EW")

    login_button = tkinter.Button(text="Login", command=login)
    login_button.grid(column=0, row=4, sticky="EW")

    create_user_button = tkinter.Button(
        text="Create User", command=create_user)
    create_user_button.grid(column=1, row=4, sticky="EW")

    """Shows the link to the currently selected Graph"""
    open_graph = tkinter.Button(
        text="Open Graph in Browser", command=open_graph)
    open_graph.grid(column=0, row=5, columnspan=2, sticky="EW")

    window.mainloop()
