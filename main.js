// Modules to control application life and create native browser window
const { app, BrowserWindow ,Menu} = require('electron');
// let python2 = require('python-shell');
// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow



//Main Menu 

const mainMenuTemp = [];


if (process.env.NODE_ENV!=='production') 
{
    mainMenuTemp.push({
        label:"Dev Tools",
        submenu : [
            {
                label:'Toggle Dev Tools',
                accelerator: process.platform == 'darwin'? 'Command+I' : 'Ctrl+I' , 
                click(item,focusedWindow){ focusedWindow.toggleDevTools();}
            },
            {
                role:'reload'
            }
        ]
    });    
}













function createWindow() {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    icon: './assets/images/8.png',
  })
  mainWindow.maximize();
  // and load the index.html of the app.
  mainWindow.loadFile('index.html')



  // Open the DevTools.
  const mainMenu = Menu.buildFromTemplate(mainMenuTemp) ;
  // Insert Menu 
  Menu.setApplicationMenu(mainMenu);








  // Emitted when the window is closed.
  mainWindow.on('closed', function () {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null
  })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {

  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', function () {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    createWindow()
  }
})







