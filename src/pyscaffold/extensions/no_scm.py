# -*- coding: utf-8 -*-
"""
Extension that omits the creation of git repository
"""

from ..api import Extension
from ..api import helpers


class NoSCM(Extension):
    """Omit creation of git (SCM) repository"""
    def activate(self, actions):
        """Activate extension

        Args:
            actions (list): list of actions to perform

        Returns:
            list: updated list of actions
        """
#        actions = helpers.register(actions, self.mynewaction,
#                                   after='create_structure')
        actions = helpers.unregister(actions, 'init_git')
        return actions

# N.B. This may be needed to fake in a version number; disable for now

#    def mynewaction(self, struct, opts):
#        """Perform some actions that modifies the structure and options
#
#        Args:
#            struct (dict): project representation as (possibly) nested
#                :obj:`dict`.
#            opts (dict): given options, see :obj:`create_project` for
#                an extensive list.
#
#        Returns:
#            struct, opts: updated project representation and options
#        """
#        ....
#        return new_actions, new_opts
