// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0

import QtQuick 6.2
import QtQuick.Window 6.2
import QTDesignerTest

Window {
    width: mainScreen.width
    height: mainScreen.height

    visible: true
    title: "QTDesignerTest"

    Screen01 {
        id: mainScreen
    }

}

