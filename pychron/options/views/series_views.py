# ===============================================================================
# Copyright 2015 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= enthought library imports =======================
from traits.api import Button, Any, Str, List
from traitsui.api import View, UItem, VGroup, EnumEditor, Item, HGroup, TableEditor
from traitsui.table_column import ObjectColumn

from pychron.core.fits.fit_selector import CheckboxColumn
from pychron.core.pychron_traits import BorderVGroup
from pychron.envisage.icon_button_editor import icon_button_editor
from pychron.options.guide import Guide
from pychron.options.options import (
    SubOptions,
    AppearanceSubOptions,
    MainOptions,
    object_column,
    checkbox_column,
)

SHOW_STATISTICS_GROUP = BorderVGroup(
    Item("show_statistics"),
    Item("show_statistics_as_table"),
    Item("use_group_statistics"),
    Item("display_min_max"),
    label="Statistics Display",
)


class SeriesSubOptions(SubOptions):
    def traits_view(self):
        v = View(
            VGroup(
                BorderVGroup(
                    "use_time_axis",
                    Item("error_bar_nsigma"),
                    Item("end_caps"),
                    Item("show_info"),
                ),
                SHOW_STATISTICS_GROUP,
            )
        )
        return v


class SeriesAppearance(AppearanceSubOptions):
    def traits_view(self):
        ee = HGroup(
            Item("error_info_fontname", label="Error Info"),
            Item("error_info_fontsize", show_label=False),
        )

        fgrp = VGroup(
            UItem("fontname"),
            self._get_xfont_group(),
            self._get_yfont_group(),
            ee,
            label="Fonts",
            show_border=True,
        )

        g = VGroup(self._get_bg_group(), self._get_padding_group())
        return self._make_view(VGroup(g, fgrp))


class SeriesMainOptions(MainOptions):
    def _get_columns(self):
        cols = [
            checkbox_column(name="plot_enabled", label="Use"),
            object_column(name="name", width=130, editor=EnumEditor(name="names")),
            object_column(name="scale"),
            object_column(name="fit", editor=EnumEditor(name="fit_types")),
            object_column(name="height", format_func=lambda x: str(x) if x else ""),
            checkbox_column(name="show_labels", label="Labels"),
            checkbox_column(name="x_error", label="X Err."),
            checkbox_column(name="y_error", label="Y Err."),
            checkbox_column(name="ytick_visible", label="Y Tick"),
            checkbox_column(name="ytitle_visible", label="Y Title"),
            checkbox_column(name="use_dev", label="Dev"),
            checkbox_column(name="use_percent_dev", label="Dev %")
            # checkbox_column(name='has_filter', label='Filter', editable=False)
        ]

        return cols


class GuidesOptions(SubOptions):
    add_guide_button = Button
    delete_guide_button = Button
    selected = Any

    def __init__(self, *args, **kw):
        super(GuidesOptions, self).__init__(*args, **kw)
        for g in self.model.guides:
            g.plotnames = list(reversed(self.model.get_aux_plot_names()))

    def _add_guide_button_fired(self):
        if self.selected:
            g = Guide(**self.selected.to_kwargs())
        else:
            g = Guide()

        g.plotnames = self.model.get_aux_plot_names()
        self.model.guides.append(g)

    def _delete_guide_button_fired(self):
        if self.selected:
            self.model.guides.remote(self.selected)

    def traits_view(self):
        cols = [
            CheckboxColumn(name="visible", label="Visible"),
            ObjectColumn(name="value", label='Value', width=200),
            ObjectColumn(name="orientation", label='Orientation'),
            ObjectColumn(name='plotname',
                         editor=EnumEditor(name='plotnames'),
                         label='Plot')
            # ObjectColumn(name="alpha", label="Opacity"),
            # ObjectColumn(name="color", label="Color"),
            # ObjectColumn(name="line_style", label='Style'),
            # ObjectColumn(name="line_width", label='Width'),
        ]
        edit_view = View(Item('label', label='Label'),
                         Item('alpha', label='Opacity'),
                         UItem('color'),
                         UItem("line_style", label='Style'),
                         UItem("line_width", label='Width'),
                         )
        return self._make_view(VGroup(HGroup(icon_button_editor('controller.add_guide_button', 'add'),
                                             icon_button_editor('controller.delete_guide_button', 'delete',
                                                                enabled_when='controller.selected')),
                                      UItem('guides', editor=TableEditor(columns=cols,
                                                                         sortable=False,
                                                                         edit_view=edit_view,
                                                                         orientation="vertical",
                                                                         selected='controller.selected'))))


# ===============================================================
# ===============================================================
VIEWS = {
    "main": SeriesMainOptions,
    "series": SeriesSubOptions,
    "appearance": SeriesAppearance,
    'guides': GuidesOptions,
}
# VIEWS['series'] = SeriesSubOptions
# VIEWS['appearance'] = SeriesAppearance


# ===============================================================
# ===============================================================


# ============= EOF =============================================
