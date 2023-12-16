// Stop watching for the system color scheme.
DarkReader.auto(false);

// Get the generated CSS of Dark Reader returned as a string.
const CSS = await DarkReader.exportGeneratedCSS();

// Check if Dark Reader is enabled.
const isEnabled = DarkReader.isEnabled();

function toggleDarkMode() {
    if (DarkReader.isEnabled()) {
        DarkReader.disable();
    } else {
        DarkReader.enable({
            brightness: 100,
            contrast: 90,
            sepia: 10
        });
        
    }

}

// Asigna la función al evento click del botón
document.getElementById('darkModeToggle').addEventListener('click', toggleDarkMode);
