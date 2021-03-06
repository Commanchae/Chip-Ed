const electron = require('electron');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu} = electron;


let mainWindow;

// listening for the app


app.on('ready', function(){
    mainWindow = new BrowserWindow({});
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, "/templates/mainWindow.html"),
        protocol: 'file',
        slashes: true
    }));

    //Build menu from template
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate)
    //Inseerting the menu
    Menu.setApplicationMenu(mainMenu)
});



// Creating menu for mainWindow


const mainMenuTemplate = [
    {
        label: 'File'
    }
]