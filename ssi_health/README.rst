.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======
Health
======

Health master data foundation: Disease Category, Disease, Allergen Category, Allergen,
Allergen Reaction, Medication, and Health Provider Role.

This module also ships two ``res.partner.category`` markers used to classify contacts
as health-related: ``ssi_health.res_partner_category_health_practitioner`` (Health
Practitioner) and ``ssi_health.res_partner_category_health_facility`` (Health
Facility). Both are root categories with no ``parent_id`` — client deployments are
free to hang their own sub-categories underneath.

**Usage contract for the two markers.** ``res.partner.category`` is hierarchical:
consumers **must** reference either marker by its module-prefixed external ID
(``ssi_health.res_partner_category_health_facility``) and filter with the
**``child_of``** domain operator — **never** ``=``. Using ``=`` matches only the exact
root record and silently drops any client sub-category nested underneath it, e.g.::

    domain = [("category_id", "child_of",
               ref("ssi_health.res_partner_category_health_facility"))]


Work Instruction
=================

Disease Category
-----------------

* `Create Disease Category <docs/health_disease_category/01-create.html>`_
* `Edit Disease Category <docs/health_disease_category/02-edit.html>`_
* `Delete Disease Category <docs/health_disease_category/03-delete.html>`_
* `Deactivate Disease Category <docs/health_disease_category/04-deactivate.html>`_
* `Activate Disease Category <docs/health_disease_category/05-activate.html>`_

Disease
--------

* `Create Disease <docs/health_disease/01-create.html>`_
* `Edit Disease <docs/health_disease/02-edit.html>`_
* `Delete Disease <docs/health_disease/03-delete.html>`_
* `Deactivate Disease <docs/health_disease/04-deactivate.html>`_
* `Activate Disease <docs/health_disease/05-activate.html>`_

Allergen Category
------------------

* `Create Allergen Category <docs/health_allergen_category/01-create.html>`_
* `Edit Allergen Category <docs/health_allergen_category/02-edit.html>`_
* `Delete Allergen Category <docs/health_allergen_category/03-delete.html>`_
* `Deactivate Allergen Category <docs/health_allergen_category/04-deactivate.html>`_
* `Activate Allergen Category <docs/health_allergen_category/05-activate.html>`_

Allergen
---------

* `Create Allergen <docs/health_allergen/01-create.html>`_
* `Edit Allergen <docs/health_allergen/02-edit.html>`_
* `Delete Allergen <docs/health_allergen/03-delete.html>`_
* `Deactivate Allergen <docs/health_allergen/04-deactivate.html>`_
* `Activate Allergen <docs/health_allergen/05-activate.html>`_

Allergen Reaction
------------------

* `Create Allergen Reaction <docs/health_allergen_reaction/01-create.html>`_
* `Edit Allergen Reaction <docs/health_allergen_reaction/02-edit.html>`_
* `Delete Allergen Reaction <docs/health_allergen_reaction/03-delete.html>`_
* `Deactivate Allergen Reaction <docs/health_allergen_reaction/04-deactivate.html>`_
* `Activate Allergen Reaction <docs/health_allergen_reaction/05-activate.html>`_

Medication
-----------

* `Create Medication <docs/health_medication/01-create.html>`_
* `Edit Medication <docs/health_medication/02-edit.html>`_
* `Delete Medication <docs/health_medication/03-delete.html>`_
* `Deactivate Medication <docs/health_medication/04-deactivate.html>`_
* `Activate Medication <docs/health_medication/05-activate.html>`_

Health Provider Role
----------------------

* `Create Health Provider Role <docs/health_provider_role/01-create.html>`_
* `Edit Health Provider Role <docs/health_provider_role/02-edit.html>`_
* `Delete Health Provider Role <docs/health_provider_role/03-delete.html>`_
* `Deactivate Health Provider Role <docs/health_provider_role/04-deactivate.html>`_
* `Activate Health Provider Role <docs/health_provider_role/05-activate.html>`_


Installation
============

To install this module, you need to:

1.  Clone the branch 14.0 of the repository https://github.com/open-synergy/ssi-health
2.  Add the path to this repository in your configuration (addons-path)
3.  Update the module list (Must be on developer mode)
4.  Go to menu *Apps -> Apps -> Main Apps*
5.  Search For *Health*
6.  Install the module


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/ssi-health/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.


Credits
=======

Contributors
------------

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by the PT. Simetri Sinergi Indonesia.
