from jnius import autoclass

def open_settings():

    PythonActivity = autoclass(
        'org.kivy.android.PythonActivity'
    )

    Intent = autoclass(
        'android.content.Intent'
    )

    Settings = autoclass(
        'android.provider.Settings'
    )

    activity = PythonActivity.mActivity

    intent = Intent(Settings.ACTION_SETTINGS)

    activity.startActivity(intent)

    return "Opening Android Settings"
