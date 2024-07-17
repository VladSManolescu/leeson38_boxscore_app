import connection_to_db as db
import sys
from game_start_window import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets



def initialise_game():
    pass


def add_teams_to_combo(ui: Ui_MainWindow, teams: list):
    possible_teams = [item['team_name'] for item in teams]
    print(possible_teams)
    ui.combo_home.addItems(possible_teams)
    ui.combo_away.addItems(possible_teams)
    ui.combo_home.currentIndexChanged.connect(change_current_team)
    ui.combo_away.currentIndexChanged.connect(change_current_team)
    # TODO look how to send parameters using connect for cleaner code



def change_current_team():
    ui.hide_elements(ui.checkbox_home_list)
    change_color_label()
    query = f"""select shirt_number from basket.players p
                inner join basket.teams t on t.team_id = p.team_id 
                where t.team_name = '{ui.combo_home.currentText()}'"""
    players = db.select_data_from_db(config, query)
    for index, player in enumerate(players):
        ui.checkbox_home_list[index].show()
        ui.checkbox_home_list[index].setText(str(player['shirt_number']))





def change_color_label():
    current_home_team = ui.combo_home.currentText()
    color_home = "black"
    for team in teams:
        if team['team_name'] == current_home_team:
            color_home = team['home_color']
            break

    # ui.team_home_label.setText("ala bala portocala")
    ui.team_home_label.setStyleSheet(f"color: {color_home};")

    current_away_team = ui.combo_away.currentText()
    color_away = "black"
    for team in teams:
        if team['team_name'] == current_away_team:
            color_away = team['away_color']
            break
    ui.team_away_label.setStyleSheet(f"color: {color_away};")




if __name__ == '__main__':
    config = db.read_config()
    teams = db.select_data_from_db(config)


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    qpixmap = QtGui.QPixmap("basketball.png")
    ui.logo_image.setPixmap(qpixmap)
    add_teams_to_combo(ui, teams)



    MainWindow.show()
    sys.exit(app.exec())
